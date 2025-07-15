from agents import Agent , Runner
from main import config

agent = Agent(
    name ='Helpful Assistant',
    instructions='You are a Helpful Assistant'
    
)

Run = Runner.run_sync(
    agent,
    'tell me top 5 colleges in karachi',
    run_config=config
)

print(Run.final_output)