import requests

parameters = {
    "lat": 41.299496,
    "lng": 69.240074,
    "formatted": 0
}
response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunset)