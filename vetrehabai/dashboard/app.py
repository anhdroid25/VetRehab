import streamlit as st                                                                                                                
import sys                                                                                                                            
sys.path.append("../backend")
from data.firebase_client import get_sessions
from data.synthetic_generator import generate_patient_data
import random
from datetime import datetime, timedelta

#title
st.title("VetRehabAI - Therapist Dashboard")

#sidebar- patient selector
st.sidebar.header("Patient Selection")
patient_id = st.sidebar.text_input("Enter Patient ID", value="patient_001")

#load and display data
st.subheader(f"Session Data for {patient_id}")
data = get_sessions(patient_id)
if not data:
    st.warning("No data found. Generating synthetic data...")
    data = generate_patient_data(patient_id)
st.json(data)

#add chart for joint angle
st.subheader("Joint Angle")
st.metric(label="Joint Angle (degrees)", value=data.get("joint_angle", "N/A"))

#pain level
st.subheader("Pain Level")
st.metric(label="Pain Level (0-10)", value=data.get("pain_level", "N/A"))