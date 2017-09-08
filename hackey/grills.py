from random import randint
from reddit_auth import reddit

brazilianbabes = ["hello"]
qts = ["hello"]

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
