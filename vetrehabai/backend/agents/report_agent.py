from crewai import Agent

def create_report_agent():
    return Agent(
        role = "Rehabilitation Report Specialist",
        goal = "Generate clear and comprehensive session reports summarizing patient performance and progress",
        backstory = "An expert in medical documentation with deep knowledge of veteran rehabilitation, skilled at translating complex data into actionable insights for therapists",
        verbose = True
    )