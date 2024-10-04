import smtplib
import datetime as dt
import random

my_email = "kisorparida@gmail.com"
password = "yztj qqev ukbu rdiv"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open("quotes.txt") as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)

    # print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kishorparida@outlook.com",
            msg=f"Subject:Quote\n\n{quote}",
        )
