from crewai import Agent

def create_alert_agent():
    return Agent(
        role = "Patient Safety Monitor",
        goal = "Identify and flag concerning patterns in patient rehabilitation data that require immediate therapist attention",
        backstory = "A vigilant specialist trained to detect risk factors and safety concerns in veteran rehabilitation, ensuring timely intervention when needed",
        llm="gpt-4o-mini",
        verbose = True
    )