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

destination = input("Destination: ")
dates = input("Travel dates (e.g., 2025 - 04 - 14): ")
activities = input("Preferred activities (tourism, art, beaches): ")
budget = input("Budget per day: ")
client = OpenAI(api_key= openai_api_key) 

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"

