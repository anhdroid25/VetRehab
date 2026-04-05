from crewai import Agent

def create_assessment_agent():
    return Agent(
        role="Physical Therapy Assessment Specialist",
        goal="Analyze exercise form and joint angles to assess rehabilitation progress",
        backstory="An expert in veteran physical therapy and biomechanics with years of experience evaluating movement quality and recovery outcomes",
        verbose=True
    )