import pandas as pd
import random as rd
import datetime as dt
import smtplib as email

my_email = "xxxxxx"
password = "xxxxxx"


letters = ["letter_1.txt",
           "letter_2.txt",
           "letter_3.txt"]
time = dt.datetime.now()
today = (time.month, time.day)
birthday_data = pd.read_csv("birthdays.csv")
birthday_dict = \
    {(row.month, row.day): f"{row['name']},{row.email},{row.year},{row.month},{row.day}"
     for (index, row) in birthday_data.iterrows()}
if today in birthday_dict:
    print(today[0])
    name = birthday_dict[today].split(',')[0]
    to_email = birthday_dict[today].split(',')[1]
    with open(rd.choice(letters)) as letter_file:
        letter_text = letter_file.read().replace("[NAME]", name)

    with email.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Happy Birthday {name}!!!\n\n{letter_text}"
        )

print(letter_text)

