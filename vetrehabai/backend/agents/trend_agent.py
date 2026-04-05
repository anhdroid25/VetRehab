from crewai import Agent

def create_trend_agent():
    return Agent(
        role = "Rehabilitation Trend Analyst",
        goal = "Track and analyze patient progress trends over multiple sessions",
        backstory = "A data-driven specialist in rehabilitation outcomes who identifies patterns in patient recovery data to optimize treatment plans",
        verbose = True
    )