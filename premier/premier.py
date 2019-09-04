import requests
import lxml.html
from pprint import pprint
from sys import exit
import json

teams = 'https://footballapi.pulselive.com/football/compseasons/274/teams'
fixtures = 'https://footballapi.pulselive.com/football/fixtures?comps=1' # &teams=10&compSeasons=274&page=0&pageSize=1&statuses=U,L&altIds=true

# respTeams = requests.get(teams).json()

def get_team_score_for(team_name):
    # teams = respTeams
    # for team in teams:
    #     if team["club"]["shortName"].lower() == team_name:
    #         fixtures = 'https://footballapi.pulselive.com/football/fixtures?comps=1&teams='+str(int(team["id"]))+'&compSeasons=274&page=0&pageSize=1&statuses=U,L&altIds=true'
    #         print(fixtures)
    #         fixtures_resp = requests.get(fixtures).json()
    #         print('a')
    #         print(fixtures_resp)
    #         content = fixtures_resp['content'][0]
    #         teams = content['teams']
    #         home_team = teams[0]
    #         away_team = teams[1]
    #         return home_team['team']['name'] + " " + str(int(home_team['score'])) + " " + away_team['team']['name'] + " " + str(int(away_team['score']))
