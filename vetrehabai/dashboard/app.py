import streamlit as st
import sys
import pandas as pd
sys.path.append("../backend")
from data.synthetic_generator import generate_multiple_sessions

st.title("VetRehabAI - Therapist Dashboard")

st.sidebar.header("Patient Selection")
patient_options = [f"patient_{str(i).zfill(3)}" for i in range(1, 11)]
selected_patients = st.sidebar.multiselect("Select Patients", patient_options, default=["patient_001"])

if not selected_patients:
    st.warning("Select at least one patient.")
    st.stop()

dfs = {
    pid: pd.DataFrame(generate_multiple_sessions(pid)).set_index("session_number")
    for pid in selected_patients
}

for metric, label in [("joint_angle", "Joint Angle"), ("pain_level", "Pain Level"), ("balance_score", "Balance Score")]:
    comparison = pd.DataFrame({pid: dfs[pid][metric] for pid in selected_patients})
    st.subheader(f"{label} Over Time")
    st.line_chart(comparison)

st.subheader("Averages")
cols = st.columns(len(selected_patients))
for col, pid in zip(cols, selected_patients):
    col.markdown(f"**{pid}**")
    col.metric("Avg Joint Angle", round(dfs[pid]["joint_angle"].mean(), 2))
    col.metric("Avg Pain Level", round(dfs[pid]["pain_level"].mean(), 2))
    col.metric("Avg Balance Score", round(dfs[pid]["balance_score"].mean(), 2))
