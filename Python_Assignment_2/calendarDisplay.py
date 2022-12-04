import calendar

class calendarDisplay():
    def __init__(self, year,month):
        print(calendar.month(year,month))

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))
obj = calendarDisplay(year,month)        