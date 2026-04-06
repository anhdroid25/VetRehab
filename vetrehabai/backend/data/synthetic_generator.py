import random
from datetime import datetime, timedelta

def generate_patient_data(patient_id):
    return {
        "patient_id": patient_id,
        "age": random.randint(25, 65),
        "injury_type": random.choice(["ACL tear", "rotator cuff", "TBI", "lower back", "ankle sprain"]),
        "affected_side": random.choice(["left", "right"]),
        "exercise": random.choice(["knee_extension", "shoulder_raise", "hip_flexion", "ankle_dorsiflexion", "elbow_extension", "wrist_flexion"]),
        "joint_angle": round(random.uniform(30.0, 180.0), 2),
        "range_of_motion": round(random.uniform(20.0, 160.0), 2),
        "rep_count": random.randint(1, 20),
        "hold_duration": random.randint(1, 30),
        "pain_level": random.randint(0, 10),
        "fatigue_level": random.randint(0, 10),
        "balance_score": round(random.uniform(0.0, 100.0), 2),
        "session_number": random.randint(1, 50),
        "timestamp": datetime.now().isoformat()
    }

def generate_multiple_sessions(patient_id, num_sessions=30):
    sessions = []
    for i in range(num_sessions):
        session = generate_patient_data(patient_id)
        session["session_number"] = i + 1
        session["timestamp"] = (datetime.now() - timedelta(days=num_sessions - i)).isoformat()
        sessions.append(session)
    return sessions
