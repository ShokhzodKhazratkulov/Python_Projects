import requests
import datetime as dt
API_ID = "9bba4f36"
API_KEY = "f5b982e12cac48150ddebc0468a6e01e"
NLE_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 179
AGE = 25


headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercise you did? ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NLE_Endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")
sheet_endpoint = "https://api.sheety.co/1478fa165d411ff182e37dc93fb4e640/myWorkoutTrackingSheet/workouts"
bearer_headers = {
    "Authorization": "Bearer U2hva2h6b2Q6VTJodmEyaDZiMlE2YzJodmEyaDZiMlF5TURJMA=="
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    from requests.auth import HTTPBasicAuth

    basic = HTTPBasicAuth("Shokhzod", "U2hva2h6b2Q6c2hva2h6b2QyMDI0")
    r = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=basic)
    print(r.text)
