import requests
from datetime import datetime

api_key = API_KEY
api_id = API_ID
exercise_endpoint = EXERCISE_ENPOINT

sheety_endpoint = MY_SHEETY_ENDPOINT

headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
}

sheety_header = {"Authorization": "Bearer BEARER_TOKEN_GOES_HERE"}

exercise_params = {
 "query": input("What exercise did you do today?: "),
 "gender": "male",
 "weight_kg": 68,
 "height_cm": 180.00,
 "age": 25
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
response.raise_for_status()
exercise_data = response.json()


for index in range(0, len(exercise_data["exercises"]) -1):
    print(index)
    exercise = exercise_data["exercises"][index]["name"]
    duration = exercise_data["exercises"][index]["duration_min"]
    calories = exercise_data["exercises"][index]["nf_calories"]
    sheety_params = {
        "workout": {
            "date": datetime.now().strftime("%Y/%m/%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
    sheet_response.raise_for_status()
    print(sheet_response.text)







