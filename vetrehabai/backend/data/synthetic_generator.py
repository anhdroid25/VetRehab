import random

def generate_patient_data(patient_id):
    return {
        "patient_id": patient_id,
        "age": random.randint(25,65),
        "exercise": random.choice(["knee_extension", "shoulder_raise", "hip_flexion"]),
        "joint_angle": round(random.uniform(30.0, 180.0), 2),
        "rep_count": random.randint(1, 20),
        "pain_level": random.randint(0, 10),
        "session_number": random.randint(1, 50)
    }