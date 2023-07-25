import requests
import datetime as dt
import os


parameters = {
 "query" : input("What exercises did you do ? "),
 "gender": "male",
 "weight_kg" : 41,
 "height_cm" : 167.64,
 "age" : 19
}

headers = {
    "x-app-id" : os.environ.get("APP_ID"),
    "x-app-key" : os.environ.get("API_KEY")
}


sheetyHeader = {
    "Authorization": os.environ.get("TOKEN")
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()['exercises']

date = dt.datetime.now()

for exercise in data:
    if len(data) == 0 :
        break

    sheetyParams = {
        "workout" : {
            "date" : date.strftime("%d-%b-%Y"),
            "time" : date.strftime("%I:%M %p"),
            "exercise" : exercise['name'].title(),
            "duration": str(exercise['duration_min']),
            "calories": exercise['nf_calories']
        }

    }

    response = requests.post(url="https://api.sheety.co/4376a327bdce5cd0d6a23f258a1b9588/myWorkouts/workouts", json=sheetyParams, headers=sheetyHeader)
    response.raise_for_status()
