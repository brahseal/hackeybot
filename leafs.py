import datetime

def get_countdown():
    today = datetime.date.today()
    leafs_opener = datetime.date(2017, 9, 18)
    diff = leafs_opener - today
    return str(diff.days) + " days for leafs"
