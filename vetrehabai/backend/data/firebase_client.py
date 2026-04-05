import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("data/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_session(patient_id, session_data):
    db.collection("sessions").document(patient_id).set(session_data)

def get_sessions(patient_id):
    doc = db.collection("sessions").document(patient_id).get()
    if doc.exists:
        return doc.to_dict()
    else:
        return {}