import requests
from bs4 import BeautifulSoup
import smtplib
import os

my_email = os.environ["MY_EMAIL"]
password = os.environ["PASSWORD"]
amazon_url = "https://www.amazon.com/-/zh_TW/LEVOIT-%E7%A9%BA%E6%B0%A3%E6%B8%85%E6%B7%A8%E6%A9%9F-%E9%81%A9%E7%94%A8%E6%96%BC%E5%AE%B6%E5%BA%AD-PM2-5-99-97/dp/B08R794ZMX/ref=sr_1_2?keywords=air%2Bpurifier&qid=1648624590&sprefix=%E7%A9%BA%E6%B0%A3%2Caps%2C351&sr=8-2&th=1"
amazon_url2 = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headders = {
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
response = requests.get(amazon_url, headers=headders)
amazon_page = response.text

soup = BeautifulSoup(amazon_page,"lxml")
price = soup.select_one(selector="tr td span.apexPriceToPay span.a-offscreen")
print(soup.title)
print(price.getText())
price_as_float = float(price.getText().split("$")[1])
print(price_as_float)


if price_as_float < 230:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hsh319ab@gmail.com",
            msg=f"Subject:Lower Price about Air Purifiers in Amazon at price ${price_as_float}\n\nGo buying at\n{amazon_url}\n"
    )