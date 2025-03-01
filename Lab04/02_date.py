# Write a Python program to subtract five days from current date.
def subtract_five_days():
    from datetime import date, timedelta
    dt = date.today() - timedelta(5)
    print('Current Date :', date.today())
    print('5 days before Current Date :', dt)
    
# Write a Python program to print yesterday, today, tomorrow.
def print_yesterday_today_tomorrow():
    from datetime import date, timedelta
    today = date.today()
    yesterday = today - timedelta(1)
    tomorrow = today + timedelta(1)
    print('Yesterday :', yesterday)
    print('Today :', today)
    print('Tomorrow :', tomorrow)
    
# Write a Python program to drop microseconds from datetime.
def drop_microseconds():
    from datetime import datetime
    dt = datetime.today()
    print("Current date and time: ", dt)
    dt = dt.replace(microsecond=0)
    print("Date and time after removing microseconds: ", dt)
    
# Write a Python program to calculate two date difference in seconds.
def calculate_date_difference():
    from datetime import datetime
    from dateutil import parser
    date1 = parser.parse('2015-01-01 01:00:00')
    date2 = parser.parse('2015-01-01 03:00:00')
    diff = date2 - date1
    print(diff.total_seconds())

print("\nPython program to subtract five days from current date:")    
subtract_five_days()
print("\nPython program to print yesterday, today, tomorrow:")
print_yesterday_today_tomorrow()
print("\nPython program to drop microseconds from datetime:")
drop_microseconds()
print("\nPython program to calculate two date difference in seconds:")
calculate_date_difference()
