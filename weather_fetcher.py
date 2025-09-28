import requests

API_KEY = "dfa967258e861d99d3acfb76e74d01b7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # to get Celsius
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    print(f"🌍 City: {data['name']}")
    print(f"🌡 Temperature: {data['main']['temp']}°C")
    print(f"☁️ Weather: {data['weather'][0]['description']}")
    print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
else:
    print("Error:", data.get("message", "Unable to fetch data"))
