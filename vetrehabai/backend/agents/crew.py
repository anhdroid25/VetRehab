from crewai import Crew, Task                                                                                     
from agents.assessment_agent import create_assessment_agent                                                       
from agents.trend_agent import create_trend_agent
from agents.alert_agent import create_alert_agent
from agents.report_agent import create_report_agent

def run_crew(payload):
    assessment = create_assessment_agent()
    trend = create_trend_agent()                                                                                                 
    alert = create_alert_agent()
    report = create_report_agent()

    current = payload["current_session"]
    history = payload["session_history"]
    patient_id = payload["patient_id"]

    task1 = Task(description=f"Assess exercise form and joint angles for patient {patient_id}. Current session: {current}", agent=assessment, expected_output="Assessment summary")
    task2 = Task(description=f"Analyze rehabilitation trends for patient {patient_id}. Session history: {history}", agent=trend, expected_output="Trend analysis")
    task3 = Task(description=f"Check for safety concerns for patient {patient_id}. Current session: {current}", agent=alert, expected_output="Alert report")
    task4 = Task(description=f"Generate full session report for patient {patient_id}. Current session: {current}. History: {history}", agent=report, expected_output="Full session report")

    crew = Crew(agents=[assessment, trend, alert, report], tasks=[task1, task2, task3, task4], verbose=True)
    return crew.kickoff()