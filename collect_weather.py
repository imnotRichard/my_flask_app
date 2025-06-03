#!/usr/bin/env python3
import requests
from src.app import Weather, db, app

def get_temperature():
    """
    Helper function to fetch current temperature from Open-Meteo API.
    """
    url = "https://api.open-meteo.com/v1/forecast?latitude=40.015&longitude=-105.2705&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["current_weather"]["temperature"]
    else:
        print("Failed to fetch weather")
        return None

if __name__ == "__main__":
    current_temperature = get_temperature()
    if current_temperature is not None:
        with app.app_context():
            new_entry = Weather(temperature=current_temperature)
            db.session.add(new_entry)
            db.session.commit()
            print(f"Temperature {current_temperature} C collected and saved!")
    else:
        print("No data collected.")
