from flask import Flask, request, jsonify
import cv2
from cv_pipeline.yolo_detector import YOLODetector
from cv_pipeline.pose_tracker import PoseTracker
from cv_pipeline.exercise_analyzer import ExerciseAnalyzer
from agents.crew import run_crew

app = Flask(__name__)

detector = YOLODetector()
tracker = PoseTracker()
analyzer = ExerciseAnalyzer()

@app.route("/start")
def start():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        results = detector.detect(frame)
        annotated_frame = results[0].plot()
        cv2.imshow("VetRehabAI - YOLO", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return {"status": "pipeline running"}

@app.route("/analyze", methods=["POST"])
def analyze():
    data= request.get_json()
    result = run_crew(data)
    return jsonify({"result": str(result)})

if __name__ == "__main__":
    app.run(debug=True)
