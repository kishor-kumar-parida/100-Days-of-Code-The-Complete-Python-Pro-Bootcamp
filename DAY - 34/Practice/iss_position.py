import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()
lon = data["iss_position"]["longitude"]
lat = data["iss_position"]["latitude"]

iss_position = (lon, lat)
print(iss_position)


# response code
# 1xx = hold on
# 2xx = success
# 3xx = go away
# 4xx = you screwed up
# 5xx = i screwed up
