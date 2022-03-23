import requests
from datetime import datetime
import os

APP_ID = os.environ["NT_APP_ID"]
APP_KEY = os.environ["NT_APP_KEY"]
SHT_USER = os.environ["SHT_USER_NAME"]
SHT_PASSW = os.environ["SHT_PASSWORD"]




exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_query = input("Tell me which exercise you do?")

exercise_config = {
    "query":exercise_query,
    "gender":"male",
    "weight_kg":116,
    "height_cm":177.5,
    "age":28
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
print(response.text)
result = response.json()

################### sheety part ##########################



SHEETY_ENDPOINT = 'https://api.sheety.co/9c3d8bbf95114f4832af9a29ce8aa9f0/workoutTracking/workouts'

today_date  = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(
            SHT_USER,
            SHT_PASSW,
        )
    )

    print(sheet_response.text)

####################### Let the post save ################

# # No Authentication
# sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs) # as shown in above
#
# # Basic Authentication
# sheet_response = requests.post(
#     SHEETY_ENDPOINT,
#     json=sheet_inputs,
#     auth=(
#         SHEETY_USERNAME,
#         SHEETY_PASSWORD,
#     )
# )
#
# #Bearer Token Authentication
# bearer_headers = {
#     "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet = SHEETY_ENDPOINT,
#     json=sheet_inputs,
#     headers=bearer_headers
# )
