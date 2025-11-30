import requests
import json

def get_weather(city):
    api_key = "3d8e6d3a06b8e2ea70e759b455dda866"  # <-- Correct API Key (Check once)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if API returned error
        if data.get("cod") != 200:
            print("\n❌ Error:", data.get("message"))
            return

        print("\n📌 Weather JSON Output:")
        print(json.dumps(data, indent=4))

    except Exception as e:
        print("\n⚠️ Something went wrong:", e)


# Run Program
get_weather("Delhi")
