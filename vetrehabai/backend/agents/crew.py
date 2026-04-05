from crewai import Crew, Task                                                                                     
from agents.assessment_agent import create_assessment_agent                                                       
from agents.trend_agent import create_trend_agent
from agents.alert_agent import create_alert_agent
from agents.report_agent import create_report_agent

def run_crew(patient_data):
    assessment = create_assessment_agent()
    trend = create_trend_agent()
    alert = create_alert_agent()
    report = create_report_agent()

    task1 = Task(description=f"Assess exercise form and joint angles for: {patient_data}", agent=assessment, expected_output="Assessment summary")
    task2 = Task(description=f"Analyze rehabilitation trends for: {patient_data}", agent=trend, expected_output="Trend analysis")
    task3 = Task(description=f"Check for safety concerns in: {patient_data}", agent=alert, expected_output="Alert report")
    task4 = Task(description=f"Generate session report for: {patient_data}", agent=report, expected_output="Full session report")

    crew = Crew(agents=[assessment, trend, alert, report], tasks=[task1, task2, task3, task4], verbose=True)      
    return crew.kickoff()