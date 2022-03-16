import smtplib
import datetime as dt
import random


my_email = "test@gmail.com"
password = "testtestest"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

        print(quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="test222@gmail.com",
                msg=f"Subject:Today Motivation\n\n{quote}"
        )


















# import smtplib
#
# my_email = "test@gmail.com"
# password = "testtestest"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="test22@gmail.com",


#         msg="Subject:Hello2\n\nThis is the body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1000, month=1,day=1, hour= 13)
# print(date_of_birth)
