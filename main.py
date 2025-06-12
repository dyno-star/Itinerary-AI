import requests
import json
from openai import OpenAI
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
google_api_key = os.getenv("GOOGLE_PLACES")
openai_api_key = os.getenv("OPENAI_API_KEY")


print("Please enter your travel preferences below: \n")

