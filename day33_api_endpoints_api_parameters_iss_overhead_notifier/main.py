import requests
from datetime import datetime

MY_LAT = 22.73
MY_LONG = 120.34


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunrise.split("T")[1].split(":"))
time_now = datetime.now()
print(time_now)

sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_hour)
print(sunset_hour)


