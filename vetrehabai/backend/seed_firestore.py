import os
from dotenv import load_dotenv
load_dotenv()

from data.firebase_client import db
from data.synthetic_generator import generate_multiple_sessions

patients = [
    {"id": "patient-001", "name": "James Carter", "dob": "1985-03-12"},
    {"id": "patient-002", "name": "Maria Lopez", "dob": "1992-07-25"},
]

for p in patients:
    db.collection("patients").document(p["id"]).set({
        "name": p["name"],
        "dob": p["dob"],
    })
    sessions = generate_multiple_sessions(p["id"], num_sessions=5)
    for session in sessions:
        db.collection("patients").document(p["id"]).collection("sessions").add(session)
    print(f"Added {p['name']} with 5 sessions")

print("Done!")
