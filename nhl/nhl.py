import requests
from hackey import meme_gen
from . import nhl_data

def get_mugshot(player_name):
    return nhl_data.get_mugshot(player_name)
