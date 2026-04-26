# Date and Time Arithmetic

from datetime import date, datetime, timedelta


today = date.today()

future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)

future_date = today - timedelta(days=3)
print("Date 3 days ago:", future_date)


now = datetime.now()
future_datetime = now + timedelta(hours=2)
print("Time after 2 hours:", future_datetime)
