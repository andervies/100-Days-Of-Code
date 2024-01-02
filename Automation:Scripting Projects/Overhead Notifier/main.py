import time
import requests
from datetime import datetime
from smtplib import SMTP

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
USER = "anderclace@gmail.com"
PASSWORD = "skskskskkkskks"


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG+5 >= iss_longitude >= MY_LONG-5:
        return True
    else:
        print('else')
        return True
    #Your position is within +5 or -5 degrees of the ISS position.

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunset)
    print(sunrise)
    time_now = datetime.now()
    print(time_now.hour)

    if sunrise >= time_now.hour or time_now.hour >= sunset:
        return True


#If the ISS is close to my current position
while True:
    time.sleep(60)
    if is_overhead() and is_night_time():
        connection = SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=USER,
            msg="Subject:Look Up 👆\n\n The ISS is above you in the sky."
        )
    else:
        print('not yet')

# and it is currently dark

# Then send me an email to tell me to look up.

# BONUS: run the code every 60 seconds.




