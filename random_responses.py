import ch
from random import randint
import praw

we_won_responses = ["we won", "WE FUCKING WON", "http://giant.gfycat.com/FluidFrigidAfricancivet.gif", "we won", "plan the parade", "http://i.imgur.com/sZAuMyi.gif", "THE BLUE JAYS ARE THE 2017 WORLD SERIES CHAMPIONS", "WORLD SERIES CONFIRMED", "WE WON", "PLAN THE PARADE"]
we_lost_responses = ["WE LOST", "https://cdn2.vox-cdn.com/thumbor/bXig9ueeRz29NY98jfYPjQi5WcY=/cdn0.vox-cdn.com/uploads/chorus_asset/file/6250539/Jimenez-Hutchison-Boink2.0.gif", "SELL THE TEAM", "http://4.bp.blogspot.com/-geoLTag9eT0/UfsjcNKAnbI/AAAAAAAAGd0/SCruu0o6EPQ/s1600/Melky-Error-2.gif", "This team is a joke", "WE LOST", "CANCEL PARADE", "I think i'm gonna kill myself", "brb killing myself", "kms", "This team is SHIT", "Fire Ross Atkins", "http://i.imgur.com/Q0DlMMe.gif", "black era all over again", "WE LOST", "we lost", "rip", "ugh", "I HATE THIS TEAM"]

shower_thoughts = []
shitty_LPT = []
motivation_images = []
quotes = []
jokes = []

is_waiting_response = False

reddit = praw.Reddit(client_id='TrWE7X7d7K2ltA',
                     client_secret='LxR5g38-cTDiLRxG9MLoOOxd-VE',
                     password='123456789',
                     user_agent='<macOS>:<1>:<0> (by /u/<hackeybotthrowaway>)',
                     username='hackeybotthrowaway')

subreddit = reddit.subreddit('Showerthoughts')
for submission in subreddit.hot(limit=150):
    shower_thoughts.append(submission.title)


subreddit = reddit.subreddit('ShittyLifeProTips')
for submission in subreddit.hot(limit=100):
    shitty_LPT.append(submission.title.split('LPT: ')[-1])

subreddit = reddit.subreddit('GetMotivated')
for submission in subreddit.hot(limit=500):
    if "image" in submission.title and submission.url[len(submission.url)-4] == ".":
        motivation_images.append(submission.url)

subreddit = reddit.subreddit('quotes')
for submission in subreddit.hot(limit=150):
    quotes.append(submission.title)

subreddit = reddit.subreddit('Jokes')
for submission in subreddit.hot(limit=300):
    joke = submission.title + " " + submission.selftext
    if len(joke) < 60:
        jokes.append(joke)

def get_thought():
    return shower_thoughts[randint(0, len(shower_thoughts)-1)]

def get_shitty_LPT():
    return shitty_LPT[randint(0, len(shitty_LPT)-1)]

def get_motivation_image():
    return motivation_images[randint(0, len(motivation_images)-1)]

def get_quote():
    return quotes[randint(0, len(quotes)-1)]

def get_joke():
    return jokes[randint(0, len(jokes)-1)]
