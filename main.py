import requests
import os
from twilio.rest import Client
sid = "x"
token = os.environ.get("AUTH_TOKEN")
# +15076153535
MY_LAT = 38.575
MY_LNG = 165.225
api_key = os.environ.get("OWM_API_KEY")
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "exclude": "minutely,daily,current"
}
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params= parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for i in range(0,12):
    if data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(sid, token)
    message = client.messages \
                    .create(
                        body="Bring an umbrella. It's going to rain. ",
                        from_='+15076153535',
                        to='+61412715347'
                    )
print(message.status)
