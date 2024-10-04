import smtplib

my_email = "kisorparida@gmail.com"
password = "yztj qqev ukbu rdiv"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="kishorparida@outlook.com",
        msg="Subject:hello\n\nThis is a test message.",
    )
