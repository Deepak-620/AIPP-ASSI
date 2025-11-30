import requests

def get_weather(city):
    api_key = "3d8e6d3a06b8e2ea70e759b455dda866"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") == "404":
        print("❌ Error: City not found. Please enter a valid city.")
        return

    print(f"\nCity: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Weather: {data['weather'][0]['description']}")

# Run Examples
get_weather("New York")
get_weather("xyz123")  # invalid case
