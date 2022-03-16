##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
# person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import pandas
import random
import datetime as dt
import smtplib

birthday_data = pandas.read_csv("birthdays.csv")


print(len(birthday_data))
for i in range(len(birthday_data)):
     print((birthday_data.month[i],birthday_data.day[i]))
birthday_dict = {}

for i in range(len(birthday_data)):
    birthday_dict[(birthday_data.month[i],birthday_data.day[i])] = birthday_data.name[i]+ " , " + birthday_data.email[i].strip()
print(birthday_dict)

now = dt.datetime.now()
month = now.month
day = now.day
print(month, day)

print(birthday_dict)
for key in birthday_dict.keys():
    if (month, day) == key:
        person_name = birthday_dict[key].split()[0]
        person_email = birthday_dict[key].split()[2]



letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
my_email = "test@gmail.com"
password = "testtestest"
chose_letter = random.choice(letter_list)

with open("./letter_templates/" + chose_letter) as letter:
    letter_words = letter.readlines()
letter = ""
for word in letter_words:
    letter += word
letter_with_name = letter.replace("[NAME]",person_name)



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=person_email,


        msg=f"Subject:Happy_Birthday\n\n{letter_with_name}"
    )
