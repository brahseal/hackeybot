import ch
from random import randint
import praw

brazilianbabes = ["hello"]
qts = ["hello"]

reddit = praw.Reddit(client_id='TrWE7X7d7K2ltA',
                     client_secret='LxR5g38-cTDiLRxG9MLoOOxd-VE',
                     password='123456789',
                     user_agent='<macOS>:<1>:<0> (by /u/<hackeybotthrowaway>)',
                     username='hackeybotthrowaway')

subreddit = reddit.subreddit('brazilians')

for submission in subreddit.hot(limit=150):
    brazilianbabes.append(submission.url)

sub = reddit.subreddit('gentlemanboners')

for submission in sub.hot(limit=150):
    qts.append(submission.url)

def get_brazzers():
    print("a")
    return brazilianbabes[randint(0, len(brazilianbabes)-1)]

def get_qts():
    return qts[randint(0, len(qts)-1)]
