from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

# Creating a Specific Date and Time

specific_datetime = datetime(2025, 5, 15, 20, 18, 10)
print("Specific date and time:", specific_datetime)


# Extracting Date and Time Components

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


# Formatting Dates and Times

formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
formatted_datetime = now.strftime("%d-%b-%Y %I:%M %p")


print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_datetime)
print("Formatted date and time:", formatted_datetime)