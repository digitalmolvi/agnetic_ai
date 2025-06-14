# src/utils/weather.py
import requests

def get_weather(city="Gilgit"):
    api_key = "demo"  # Replace with real key if needed
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")
    return response.json()