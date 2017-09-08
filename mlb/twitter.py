import tweepy
import datetime
import time
from . import mlb
from . import favorite_team

auth = tweepy.OAuthHandler("v3fm3b4cVtq9Z0IILLHVp8jM2", "KqPisoNSHeH2xsXa8au2QcYx432IG060CnBDErqCYHBUkRc2re")
auth.set_access_token("875603904670580737-CJlUHZtWF3Q1gldNh0sWpnTfExkKwkX", "UJVc3fmJxXZmONBOVRejcdw7b2TJXRJuoYf6VjmBwOLIK")

api = tweepy.API(auth)

def get_last_tweet_from_dome():
    if mlb.is_team_playing(favorite_team.short_name) and mlb.is_team_at_home(favorite_team.short_name):
        tweets = api.user_timeline(screen_name = 'IstheDomeOpen', count = 5)
        for tweet in tweets:
            if "OPEN" in tweet.text or "CLOSED" in tweet.text:
                if (datetime.datetime.now() - tweet.created_at).days < 1:
                    return tweet.text

        return "I don't know yet if the dome will be open man, give me more time"

    elif mlb.is_team_playing(favorite_team.short_name) and not mlb.is_team_at_home(favorite_team.short_name):
        return favorite_team.short_name + " are on the road, so who cares?"
    else:
        return favorite_team.short_name + " are not playing today, so who cares?"
