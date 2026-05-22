from crewai import Agent, Crew, LLM, Process, Task

from backend.config import LANGFUSE_ENABLED
from backend.tools.tools import (
    get_flight_prices,
    get_hotel_prices,
    get_tourist_places,
    get_weather_data,
)

langfuse = None
if LANGFUSE_ENABLED:
    from langfuse import get_client

    langfuse = get_client()
    if langfuse.auth_check():
        print("Langfuse connected")

llm = LLM(model="openai/gpt-4o-mini", temperature=0)


def travel_planner(query: str) -> str:
    weather_agent = Agent(
        role="Weather Analyst",
        goal=(
            "Provide accurate weather information using the tool for the city "
            "and particular month. Do not make up any data."
        ),
        backstory="You are a weather analyst who uses tools for factual answers.",
        llm=llm,
        tools=[get_weather_data],
        verbose=True,
    )

    flight_agent = Agent(
        role="Travel Advisor",
        goal=(
            "Provide accurate flight price data using the tool for the city "
            "and particular month. Do not make up any data."
        ),
        backstory="You help tourists with flight prices using the tool.",
        llm=llm,
        tools=[get_flight_prices],
        verbose=True,
    )

    hotel_agent = Agent(
        role="Hotel Advisor",
        goal=(
            "Provide accurate hotel prices using the tool for the city and month. "
            "Do not make up any data."
        ),
        backstory="You help tourists with hotel prices using the tool.",
        llm=llm,
        tools=[get_hotel_prices],
        verbose=True,
    )

    places_agent = Agent(
        role="Tour Guide",
        goal=(
            "Provide accurate tourist places for the city using the tool. "
            "Do not make up any information."
        ),
        backstory="You suggest famous tourist places in a city using the tool.",
        llm=llm,
        tools=[get_tourist_places],
        verbose=True,
    )

    tour_planner = Agent(
        role="Final Tour Planner",
        goal=(f"""
            Provide a final tour plan based on the user query. 
            Answer directly and suggest what clothes to pack.
            If youd did not find any information from previous agents just say you dont have information
            """
        ),
        backstory="You synthesize specialist reports into one helpful trip plan.",
        llm=llm,
        verbose=True,
    )

    task_weather = Task(
        description=(
            f"Provide accurate weather data for the city and month in this query: {query}. "
            "Include temperature and weather condition."
        ),
        agent=weather_agent,
        expected_output="Accurate weather data for the city and month.",
    )

    task_flight = Task(
        description=(
            f"Provide accurate round-trip flight prices for the city and month in: {query}"
        ),
        agent=flight_agent,
        expected_output="Structured flight price data for that city and month.",
    )

    task_hotel = Task(
        description=(
            f"Provide accurate hotel price data for the city and month in: {query}"
        ),
        agent=hotel_agent,
        expected_output="Structured hotel price data for that city and month.",
    )

    task_places = Task(
        description=f"List top tourist places to visit based on: {query}",
        agent=places_agent,
        expected_output="Structured list of places to visit.",
    )

    task_planner = Task(
        description=(
            f"Answer the user's query directly using prior task outputs. "
            f"User query: {query}. "
            "Suggest clothes to pack and useful travel items when relevant."
            f"Only answer if you found information in the prior tasks and agents, do not respond with your own information."
        ),
        agent=tour_planner,
        expected_output=(
            "A direct answer to the user's question, including weather, "
            "flights, hotels, and places when available."
        ),
        context=[task_weather, task_flight, task_hotel, task_places],
    )

    crew = Crew(
        agents=[weather_agent, flight_agent, hotel_agent, places_agent, tour_planner],
        tasks=[task_weather, task_flight, task_hotel, task_places, task_planner],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    if langfuse is not None:
        langfuse.flush()

    return str(result)
