from agents import Agent , Runner , function_tool
from main import config
import os
from dotenv import load_dotenv
import requests

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")


@function_tool
def weather(city : str) -> str:
    result = requests.get(f" http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}")
    
    data = result.json()
    
    
    return f"The current weather in {city} is {data['current']['temp_c']}°C with {data['current']['condition']['text']}"

agent = Agent(
    name ='Weather Assistant',
    instructions='You are a Helpful Assistant',
    tools=[weather]
    
)

Run = Runner.run_sync(
    agent,
    'what is current weather in karachi',
    run_config=config
)

print(Run.final_output)