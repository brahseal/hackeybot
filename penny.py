from random import randint
import datetime

pennypics = ["http://i.imgur.com/c4dyhjd.png", "http://i.imgur.com/8vtqKdo.png",
 "http://i.imgur.com/xOIHJ6L.png", "http://i.imgur.com/JDTpgkB.png", "http://i.imgur.com/xIlgI1H.png"
 "http://i.imgur.com/x1TcxEn.png", "http://i.imgur.com/X8MFZAv.png", "http://i.imgur.com/9PO45fe.png",
 "http://i.imgur.com/zePRj9e.png", "http://i.imgur.com/F7wXD7i.png", "http://i.imgur.com/I9MymnA.png",
 "http://i.imgur.com/q6XVm8C.png", "http://i.imgur.com/23KMAnf.png", "http://i.imgur.com/B82u0tx.png",
 "http://i.imgur.com/aZAJibT.png", "http://i.imgur.com/qs5CpRk.png", "http://i.imgur.com/BC3R4a9.png",
 "http://i.imgur.com/xcgMiZI.png", "http://i.imgur.com/UKL9RkR.png", "http://i.imgur.com/OeruOIc.png"
 "http://i.imgur.com/2lcWEzX.png","http://i.gyazo.com/0bafa3d42ebf773da5b90d2cd6cf3f17.gif",
 "http://i.imgur.com/ZjRwYZs.jpg", "http://i.imgur.com/rbwYSuw.png","http://i.gyazo.com/0bafa3d42ebf773da5b90d2cd6cf3f17.gif",
 "http://i.imgur.com/k4hNCJ8.png", "http://i.imgur.com/NuXFjSe.png", "http://i.imgur.com/HO3yGra.png",
 "http://i.imgur.com/LJrnlU2.png", "http://i.imgur.com/ZcPao4y.png", "http://i.imgur.com/wB8FOlv.png",
 "http://i.imgur.com/4eBs0QR.png", "http://i.imgur.com/PkTxzeq.png", "http://i.imgur.com/elspcQr.png",
 "http://i.imgur.com/ZeXyPjj.png", "http://i.imgur.com/Pil6DuS.png",
 "http://i.imgur.com/r6J6Ikc.png", "http://i.imgur.com/9GuzUnl.png", "http://i.imgur.com/1l6Lsty.png",
 "http://i.imgur.com/k28XBNq.png", "http://i.imgur.com/nggiVuH.png", "http://i.imgur.com/6hR97bW.png",
 "http://i.imgur.com/7Ep2bv8.png", "http://i.imgur.com/dhJ9LCc.png", "http://i.imgur.com/bHlm9Qi.png",
 "http://i.imgur.com/TkGWhgp.png"
]

def get_random_pic():
    print("hi")
    random_pic = pennypics[randint(0, len(pennypics) -1)]
    return(random_pic)

def get_penny_dance():
    return "http://i.gyazo.com/0bafa3d42ebf773da5b90d2cd6cf3f17.gif"

def get_penny_age():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    pb = datetime.datetime(2000,6,13)
    today = datetime.datetime(year,month,day)
    years = today.year - pb.year

    months = today.month - pb.month
    if months < 0:
        years -= 1

    days = today.day - pb.day
    if days < 0:
        months-=1

    return "Penny has " + str(years) + " years " + str(months) + " month and " + str(days) + " days."
