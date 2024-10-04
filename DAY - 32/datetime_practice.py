import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

dob = dt.datetime(year=2002, month=8, day=5, hour=19, minute=45)
print(dob)
