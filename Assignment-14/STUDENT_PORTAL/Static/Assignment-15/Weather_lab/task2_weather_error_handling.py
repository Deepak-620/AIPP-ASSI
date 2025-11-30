import requests
import json

def get_weather(city):
    try:
        api_key = "3d8e6d3a06b8e2ea70e759b455dda866"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        print(json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException:
        print("❌ Error: Could not connect to API. Check your API key or network.")

# Run
get_weather("London")
