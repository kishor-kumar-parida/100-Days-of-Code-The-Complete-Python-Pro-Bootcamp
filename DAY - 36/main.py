import requests

endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "YourAPI"

weather_params = {
    "lat": 13.082680,
    "lon": 80.270721,
    "appid": api_key,
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

condition = weather_data["weather"][0]["id"]

if int(condition == 700):
    print("Its Raining")
else:
    print("All Good")
