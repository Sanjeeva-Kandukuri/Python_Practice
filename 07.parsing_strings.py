# Parsing Strings into Dates

from datetime import datetime

date_string = "16-05-2025 14:30"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M")

print(parsed_date)
