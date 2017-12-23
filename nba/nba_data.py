import nba_py
import requests
import json

teams_dictionary = { 
    'hawks': '1610612737',
    'celtics': '1610612738',
    'nets': '1610612751',
    'hornets': '1610612766',
    'bulls': '1610612741',
    'cavs': '1610612739',
    'mavericks': '1610612742',
    'nuggets': '1610612743',
    'pistons': '1610612765',
    'gsw': '1610612744',
    'warriors': '1610612744',
    'rockets': '1610612745',
    'pacers': '1610612754',
    'clippers': '1610612746',
    'lakers': '1610612747',
    'grizzlies': '1610612763',
    'heat': '1610612748',
    'bucks': '1610612749',
    'timberwolves': '1610612750',
    'pelicans': '1610612740',
    'knicks': '1610612752',
    'thunder': '1610612760',
    'magic': '1610612753',
    'sevensixers': '1610612755',
    'suns': '1610612756',
    'blazers': '1610612757',
    'kings': '1610612758',
    'spurs': '1610612759',
    'raps': '1610612761',
    'raptors': '1610612761',
    'craps': '1610612761',
    'jazz': '1610612762',
    'wizards': '1610612764' 
}

def get_score_from_team(team_name):
    team_id = teams_dictionary[team_name]
    if not team_id:
        return "Couldn't find the score for todays game"
    url = 'https://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2017/scores/00_todays_scores.json'
    json = requests.get(url).json()
    games = json['gs']['g']
    for game in games:
        home_team_id = game['h']['tid']
        visitor_team_id = game['v']['tid']
        if home_team_id == int(team_id) or visitor_team_id == int(team_id):
            home_team_score = game['h']['s']
            visitor_team_score = game['v']['s']
            home_team_name = game['h']['tc'] + " " + game['h']['tn']
            visitor_team_name = game['v']['tc'] + " " + game['v']['tn']
            output = home_team_name + " " + str(home_team_score) + " - " + visitor_team_name + " " + str(visitor_team_score)
            return output    