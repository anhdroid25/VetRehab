import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("data/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_session(patient_id, session_data):
    db.collection("patients").document(patient_id).collection("sessions").add(session_data)

def get_sessions(patient_id):
    docs = db.collection("patients").document(patient_id).collection("sessions").stream()
    return [doc.to_dict() for doc in docs]
    
def get_all_patients():
    docs = db.collection("patients").stream()
    return [doc.id for doc in docs]
