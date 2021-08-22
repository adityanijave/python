# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

year = int(input("Enter the year : "))
month = int(input("enter the month : "))
calendar.setfirstweekday(calendar.SUNDAY)
calendar = calendar.month(year,month)
print(f"\n{calendar}")