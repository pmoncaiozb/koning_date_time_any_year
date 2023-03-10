import datetime
import calendar

def find_day(date):
    kon = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return calendar.day_name[kon]

print("The day of the week is " + find_day("11 10 2023"))