import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWN_API_KEY")
account_sid = "AC5ff15d4a4ea82825f99cf0f748e0ba8d"
auth_token = os.environ.get("OWN_AUTH_TOKEN")
url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
valid_url = "https://api.openweathermap.org/data/2.5/onecall?lat=22.627277&lon=120.301437&exclude={" \
            "part}&appid=d57ac72e6973b83780ccf9ab2a0ec2ea "
parameters = {
    "lat":22.627277,
    "lon":120.301437,
    "exclude": "current,minutely,daily",
    "appid":api_key,

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:48]

will_rain = False
for hour_data in weather_slice:
    condition_code =hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain tomorrow or Tuesday. Remember to bring an ☂︎",
        from_='+18126246802',
        to='Your Phone Number'
    )
print(message.status)
# hourly_weather = weather_data["hourly"]
#
# for num, item in enumerate(hourly_weather):
#     if item["weather"][0]["id"] < 700:
#         print(f"At {num} hours later, bring an umbrella")
