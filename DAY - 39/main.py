import requests
from datetime import datetime

# Nutritionix personal data
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 22

# Nutritionix API Credentials
NIX_APP_ID = "7de66b94"
NIX_API_KEY = "bbb88bf851fcfba056497d0375eb08f3"

# Sheety Project API Credentials
SHEETY_ENDPOINT = (
    "https://api.sheety.co/6e283b17510cc82924120efc25b275c0/myWorkoutsDiary/workouts"
)
SHEETY_USERNAME = "kishor"
SHEETY_PASSWORD = "Kishor@2002"

# Exercise input
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Nutritionix API headers
headers = {
    "x-app-id": NIX_APP_ID,
    "x-app-key": NIX_API_KEY,
}

# Nutritionix API parameters
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Make a POST request to Nutritionix API
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()  # Check for request errors

# Parse the result from Nutritionix
result = response.json()
print(f"Nutritionix API call: \n{result}\n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Google Sheet entry format
GOOGLE_SHEET_NAME = "workout"

# Sending data to Sheety
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # Sending the data to Sheety using Basic Auth
    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
    )

    # Print the response from Sheety API
    print(f"Sheety Response: \n{sheet_response.text}")
