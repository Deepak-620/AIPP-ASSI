import requests
import json
import os

def get_weather_and_store(city):
    api_key = "3d8e6d3a06b8e2ea70e759b455dda866"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather_info = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"]
    }

    print(json.dumps(weather_info, indent=4))

    file_name = "results.json"

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.append(weather_info)

    with open(file_name, "w") as file:
        json.dump(existing_data, file, indent=4)

# Run
get_weather_and_store("Delhi")
