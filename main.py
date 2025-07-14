import os
from dotenv import load_dotenv
from agents import AsyncOpenAI , OpenAIChatCompletionsModel , Runner , RunConfig

load_dotenv()
gemini_Api_Key = os.getenv('GEMINI_API_KEY')

if not gemini_Api_Key :
    raise ValueError("GEMINI_API_KEY is not set. please ensure set Api Key.")

external_client = AsyncOpenAI(
    api_key = gemini_Api_Key,
    base_url= 'https://generativelanguage.googleapis.com/v1beta/openai',
)

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = external_client 
)

config = RunConfig(
    model = model,
    provider = external_client,
    tracing_disabled = True
)