import requests


api_key = "9854eb105524c9fb307ed68f86845852"
api_key2 = "0725c2aedbcb486145f6b4dfc7c5236d"

parameters = {
    "lat": 9.076479,
    "lon": 7.398574,
    "appid": api_key2
}

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"


response = requests.get(url=OWM_endpoint, params=parameters)
print(response.status_code)
feedback = response.json()
print(feedback)




