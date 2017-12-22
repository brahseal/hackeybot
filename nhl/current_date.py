import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

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

def get_tomorrow():
    today = datetime.now().strftime('%m-%d')
    tomorrow = datetime.now()+ relativedelta(days=1)
    return str(tomorrow.strftime('%m-%d'))

def get_five_days_from_now():
    today = datetime.now().strftime('%m-%d')
    five_days_from_now = datetime.now()+ relativedelta(days=5)
    return str(five_days_from_now.strftime('%m-%d'))


def get_hour():
    return time.strftime("%H")

def convert_str(s):
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret

def get_weekday_from(date):
    weekday = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
    return weekday
