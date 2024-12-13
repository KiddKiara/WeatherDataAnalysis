import requests
import pandas as pd
import logging

# Your API key
API_KEY = "7959c89c2c0d914527ab20c8e35d7bb1"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# List of cities
cities = ["London", "New York", "Tokyo", "Delhi", "Sydney", "Cairo", "Paris", "Moscow", "Rio", "Cape Town"]

# Store weather data
weather_data = []

for city in cities:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "City": city,
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        })
    else:
        print(f"Failed to fetch data for {city}: {response.status_code}")

# Set up logging
logging.basicConfig(filename="weather_data.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Example log messages
logging.info("Starting to fetch weather data...")
for city in cities:
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        logging.info(f"Successfully fetched data for {city}")
    except Exception as e:
        logging.error(f"Failed to fetch data for {city}: {e}")

# Save data to a CSV file
df = pd.DataFrame(weather_data)
df.to_csv("weather_data.csv", index=False)
print("Weather data saved to weather_data.csv")
