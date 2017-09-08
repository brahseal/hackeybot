import datetime

lou = ["https://media.giphy.com/media/bGcJcUnTt77uE/giphy.gif", "http://betweentheposts.ca/wp-content/uploads/2016/11/16-lougodfatheredited-X-V.jpg",
        "https://streamable.com/nhb9i", "http://i.imgur.com/bEzt7Vj.jpg"]

def get_countdown():
    today = datetime.date.today()
    leafs_opener = datetime.date(2017, 9, 18)
    diff = leafs_opener - today
    return str(diff.days) + " days for leafs"
