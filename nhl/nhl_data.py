#THX THEAVS
import requests
import lxml.html
from pprint import pprint
from sys import exit
import json
import csv

url = 'http://www.nhl.com/stats/rest/grouped/skaters/basic/season/bios?cayenneExp=gameTypeId=%222%22%20and%20seasonId%3E=20162017%20and%20seasonId%3C=20162017&factCayenneExp=gamesPlayed%3E=60&sort=[{%22property%22:%22playerBirthDate%22,%22direction%22:%22DESC%22}]'

resp = requests.get(url).text
resp = json.loads(resp)

def get_mugshot(player_name):
	for x in range(0, len(resp['data'])):
		if resp['data'][x]['playerLastName'].lower() == player_name:
			return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(resp['data'][x]['playerId']) + '.jpg')
