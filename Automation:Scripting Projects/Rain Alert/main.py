import requests


api_key = API_KEY
api_key2 = API_KEY_2

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key2
}

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"


response = requests.get(url=OWM_endpoint, params=parameters)
print(response.status_code)
feedback = response.json()
print(feedback)




