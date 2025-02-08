import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
url = "https://www.alphavantage.co/query"
api_key = API_KEY

day_before = datetime.today().date() - timedelta(2)
yesterday = datetime.today().date() - timedelta(1)

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": api_key
}

news_parameters = {
    "function": "NEWS_SENTIMENT",
    "tickers": COMPANY_NAME,
    "apikey": api_key,
    "limit": 3
}

stock_response = requests.get(url=url, params=stock_parameters)
news_response = requests.get(url=url, params=news_parameters).json()
print(news_response)

day_before_data = stock_response.json()["Time Series (Daily)"][f'{day_before}']
yesterdays_data = stock_response.json()["Time Series (Daily)"][f'{yesterday}']

day_before_closing_stock = float(day_before_data["4. close"])
yesterdays_closing_stock = float(yesterdays_data["4. close"])

change_in_stock = (day_before_closing_stock - yesterdays_closing_stock) / day_before_closing_stock * 10


print(day_before_data)
print(yesterdays_closing_stock)
print(day_before_closing_stock)
print(change_in_stock)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if abs(change_in_stock) >= 5:
    print("Get news")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

