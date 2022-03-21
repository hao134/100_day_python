import os
import math
from twilio.rest import Client
import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_api_key = "06d500437a084834a32b0bfba1bffe19" #os.environ.get("NEWS_API_KEY")
stock_api_key = "6CSMVY5U1I7KO9FE" #os.environ.get("STOCK_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":stock_api_key
}
stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={stock_api_key}'
stock_response = requests.get("https://www.alphavantage.co/query",params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
today = datetime.today()

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.
def check_not_holiday(day):
    if day.weekday() == 6 or day.weekday() == 5:
        return False

def judge_case(TODAY):
    if TODAY.weekday() == 0:
        return "case_monday"
    elif TODAY.weekday() == 1:
        return "case_tuesday"
    elif TODAY.weekday() == 6:
        return "case_sunday"
    else:
        return "case_normal"

if judge_case(today) == "case_monday":
    lastday = datetime.today() - timedelta(days=3)
    two_days_ago = datetime.today() - timedelta(days=4)
elif judge_case(today) == "case_tuesday":
    lastday = datetime.today() - timedelta(days=1)
    two_days_ago = datetime.today() - timedelta(days=4)
elif judge_case(today) == "case_sunday":
    lastday = datetime.today() - timedelta(days=2)
    two_days_ago = datetime.today() - timedelta(days=3)
else:
    lastday = datetime.today() - timedelta(days=1)
    two_days_ago = datetime.today() - timedelta(days=2)

Lastday = lastday.strftime('%Y-%m-%d')
Two_days_ago = two_days_ago.strftime('%Y-%m-%d')
stock_daily_data = stock_data['Time Series (Daily)']
lastday_close_stock = stock_daily_data[Lastday]["4. close"]
twodays_close_stock = stock_daily_data[Two_days_ago]["4. close"]
change_ranting = (float(lastday_close_stock) - float(twodays_close_stock))/float(lastday_close_stock)

print(f"last day: {lastday.strftime('%m-%d')},\n {stock_daily_data[Lastday]}")
print(lastday_close_stock)
print(twodays_close_stock)
print(change_ranting)
if change_ranting > 0.03:
    print("Get News.")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news_parameters = {
    "q": "TSLA",
    "apikey":news_api_key
}

news_response = requests.get("https://newsapi.org/v2/everything",params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)
if change_ranting > 0.03:
    print("The lastest 3 News Title: ")
    for news in news_data["articles"][:3]:
        print(news["title"])


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
account_sid = "AC5ff15d4a4ea82825f99cf0f748e0ba8d"
auth_token = os.environ.get("OWN_AUTH_TOKEN")
news_title = news_data["articles"][0]["title"]
brief_content = news_data["articles"][0]["content"][:134]
print(news_title)
print(brief_content)

# if will_rain:
#     print("Bring an umbrella")
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It's going to rain tomorrow or Tuesday. Remember to bring an ☂︎",
#         from_='+18126246802',
#         to='Your Phone Number'
#     )


if float(lastday_close_stock) - float(twodays_close_stock) > 0:
    print(f"TSLA: 🔺{math.floor(change_ranting*100)}%\nHeadline:{news_title}\nBrief:{brief_content}")
else:
    print(f"TSLA: 🔻{math.floor(change_ranting*100)}%\nHeadline:{news_title}\nBrief:{brief_content}")

body_message = f"TSLA: 🔺{math.floor(change_ranting*100)}%\nHeadline:{news_title}\nBrief:{brief_content}"

client = Client(account_sid, auth_token)
message = client.messages.create(
        body= body_message,
        from_='+18126246802',
        to='Your Home Number'
)
print(message.status)


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

