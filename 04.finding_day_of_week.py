from datetime import date 
today = date.today()
print("Weekday (0=Monady, 6=Sunday):", today.weekday())
print("IOS Weekday (1=Monday, 7=Sunday):", today.isoweekday())