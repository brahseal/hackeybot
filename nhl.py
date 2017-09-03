import requests
import meme_gen

def get_mugshot(player_name):
    response = requests.get("http://nhl.nickoman.me/images/"+player_name)
    mugshot = meme_gen.get_avi(response.text)
    return mugshot
