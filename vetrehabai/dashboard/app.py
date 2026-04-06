import streamlit as st
import sys
import pandas as pd
sys.path.append("../backend")
from data.synthetic_generator import generate_multiple_sessions

st.title("VetRehabAI - Therapist Dashboard")

st.sidebar.header("Patient Selection")
patient_id = st.sidebar.text_input("Enter Patient ID", value="patient_001")

sessions = generate_multiple_sessions(patient_id)
df = pd.DataFrame(sessions)

st.subheader(f"Sessions for {patient_id}")
st.dataframe(df)

st.subheader("Joint Angle Over Time")
st.line_chart(df.set_index("session_number")["joint_angle"])

st.subheader("Pain Level Over Time")
st.line_chart(df.set_index("session_number")["pain_level"])

st.subheader("Balance Score Over Time")
st.line_chart(df.set_index("session_number")["balance_score"])

col1, col2, col3 = st.columns(3)
col1.metric("Avg Joint Angle", round(df["joint_angle"].mean(), 2))
col2.metric("Avg Pain Level", round(df["pain_level"].mean(), 2))
col3.metric("Avg Balance Score", round(df["balance_score"].mean(), 2))
