import helper
import time

def get_year():
    return helper.convert_str(time.strftime("%Y"))

def get_month():
    return helper.convert_str(time.strftime("%m"))

def get_day():
    hour = helper.convert_str(time.strftime("%H"))
    day = day = helper.convert_str(time.strftime("%d"))
    # rewing the day if it's not past 11 a.m (need to check if month is turning)
    if hour < 10:
        day -= 1
    print(day)
    print(hour)
    return day

def get_hour():
    return helper.convert_str(time.strftime("%H"))
