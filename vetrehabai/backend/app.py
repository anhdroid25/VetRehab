from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
import cv2
from cv_pipeline.yolo_detector import YOLODetector
from cv_pipeline.pose_tracker import PoseTracker
from cv_pipeline.exercise_analyzer import ExerciseAnalyzer
from agents.crew import run_crew
from data.firebase_client import get_sessions

app = Flask(__name__)

detector = YOLODetector()
tracker = PoseTracker()
analyzer = ExerciseAnalyzer()

@app.route("/start")
def start():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = detector.detect(frame)
        annotated_frame = results[0].plot()
        pose_results = tracker.track(frame)
        if pose_results and pose_results.pose_landmarks:
            landmarks = pose_results.pose_landmarks.landmark
            a = [landmarks[11].x, landmarks[11].y]
            b = [landmarks[13].x, landmarks[13].y]
            c = [landmarks[15].x, landmarks[15].y]
            angle = analyzer.calculate_angle(a, b, c)
            cv2.putText(annotated_frame, f"Angle: {angle:.1f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("VetRehabAI - YOLO", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return {"status": "pipeline running"}

@app.route("/analyze", methods=["POST"])
def analyze():
    data= request.get_json()
    patient_id = data.get("patient_id")
    if not patient_id:
        return jsonify({"error": "patient_id is required"}), 400
    history = get_sessions(patient_id)
    payload = {
        "patient_id": patient_id,
        "current_session": data,
        "session_history": history
    }
    result = run_crew(payload)
    return jsonify({"result": str(result)})

if __name__ == "__main__":
    app.run(debug=True)
