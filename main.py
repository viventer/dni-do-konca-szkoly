import time
from datetime import date

date_now = date.today()

if date_now.month >= 9:
    year = date_now.year + 1
elif 7 <= date_now.month <= 8 or date_now.month == 6 and date_now.day >= 24:
    print("Trwają wakacje ;)")
    exit()
elif date_now.month == 6 and date_now.day == 23:
    print("Dzisiaj zakończenie roku :D")
    exit()
else:
    year = date_now.year

school_end = date(year, 6, 23)
difference = school_end - date_now

if difference.days == 1:
    start, end = ["pozostał", "dzień"]
elif 2 <= difference.days <= 4:
    start, end = ["pozostały", "dni"]
else:
    start, end = ["pozostało", "dni"]

print("Do końca szkoły", start, difference.days,end)
