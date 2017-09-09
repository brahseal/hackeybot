#THX THEAVS
import requests
import lxml.html
from pprint import pprint
from sys import exit
import json
import csv

players = 'http://www.nhl.com/stats/rest/grouped/skaters/basic/season/skatersummary?cayenneExp=gameTypeId=%223%22%20and%20seasonId%3E=20142015%20and%20seasonId%3C=20162017&factCayenneExp=gamesPlayed%3E=1&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]'

goalies = 'http://www.nhl.com/stats/rest/grouped/goalies/goalie_basic/season/goaliesummary?cayenneExp=gameTypeId=%222%22%20and%20playerPositionCode=%22G%22%20and%20seasonId%3E=20162017%20and%20seasonId%3C=20162017&factCayenneExp=gamesPlayed%3E=1&sort=[{%22property%22:%22wins%22,%22direction%22:%22DESC%22}]'

respPlayers = requests.get(players).text
respPlayers = json.loads(respPlayers)

respGoalies = requests.get(goalies).text
respGoalies = json.loads(respGoalies)

def get_mugshot(player_name):

	for x in range(0, len(respPlayers['data'])):
		if respPlayers['data'][x]['playerLastName'].lower() == player_name:
			return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(respPlayers['data'][x]['playerId']) + '.jpg')
	
	
	for x in range(0, len(respGoalies['data'])):
		if respGoalies['data'][x]['playerLastName'].lower() == player_name:
			return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(respGoalies['data'][x]['playerId']) + '.jpg')