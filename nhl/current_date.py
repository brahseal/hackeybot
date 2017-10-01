import time

def get_year():
    return time.strftime("%Y")

def get_month():
    return time.strftime("%m")

def get_day():
    hour = convert_str(time.strftime("%H"))
    day = convert_str(time.strftime("%d"))
    # rewing the day if it's not past 11 a.m (need to check if month is turning)
    if hour < 10:
        day -= 1
    print(day)
    print(hour)
    day = str(day)
    return day

def get_hour():
    return time.strftime("%H")

def convert_str(s):
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret
