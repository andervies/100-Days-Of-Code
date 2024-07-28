import datetime as dt
import random
import smtplib


my_email = "myemail@gmail.com"
password = "sksksksksksk"

now = dt.datetime.now()
current_day = now.weekday()
print(current_day)
if current_day == 2:
    print(current_day)
    with open("quotes.txt") as quotes:
        list_of_quotes = quotes.readlines()
    quote_of_the_week = random.choice(list_of_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="youremail@gmail.com",
                            msg=f"Subject: Quote of the Week\n\n{quote_of_the_week}")







