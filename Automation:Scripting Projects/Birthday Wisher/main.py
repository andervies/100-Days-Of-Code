##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime
import random

MY_EMAIL = "anderclace@gmail.com"
MY_PASSWORD = "sksksksksksk"

# 1. Update the birthdays.csv
with open("birthdays.csv") as datafile:
    data = pandas.read_csv(datafile)



# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.date.today()
today_tuple = (today.month, today.day)

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
birthday_person = birthday_dict[today_tuple]
if today_tuple in birthday_dict:
    letter = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])

    with open(f"letter_templates/{letter}") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp@gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject: Happy Birthday\n\n{contents}")







# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




