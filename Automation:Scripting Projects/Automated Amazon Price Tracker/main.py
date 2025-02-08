import requests
from smtplib import SMTP
from bs4 import BeautifulSoup
import lxml

MY_EMAIL = EMAIL
MY_PASSWORD = PASSWORD
URL = "https://www.amazon.com/Andoer-Photography-Professional-2800-5700K-Temperature/dp/B08T61SMMH/ref=sr_1_6" \
      "?keywords=filmmaking%2Blighting%2Bequipment&qid=1691585376&sprefix=filmmaking%2Blight%2Caps%2C558&sr=8-6&th=1 "

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/16.4.1 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9",
}
target_price = 200


response = requests.get(url=URL, headers=headers)
print(response)

soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

price_text = soup.find(name="span", class_="a-offscreen").getText()
price = float(price_text.strip("$"))
print(price)

if target_price > price:
    connection = SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject: Bingo!!! Huge deal Alert!/n/n you have a great deal at {URL}")

