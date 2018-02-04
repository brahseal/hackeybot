import requests
import lxml.html
from pprint import pprint
from sys import exit
import json
import csv
from . import current_date
# import current_date
from datetime import datetime
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

year = current_date.get_year()
month = current_date.get_month()
day = current_date.get_day()

def update_time():
    global year
    year = current_date.get_year()
    global month
    month = current_date.get_month()
    global day
    day = current_date.get_day()

sched.add_interval_job(update_time, hours=6)

divisions_dictionary = {
 'metro': '0',
 'metropolitan': '0',
 'atlantic': '1',
 'central': '2',
 'pacific': '3'
}

teams_dictionary = {
 'devils': '01',
 'islanders': '02',
 'rangers': '03',
 'rags': '03',
 'flyers': '04',
 'pens': '05',
 'penguins': '05',
 'bruins': '06',
 'sabres': '07',
 'habs': '08',
 'sens': '09',
 'leafs': '10',
 #11 is not an active team
 'canes': '12',
 'hurricanes': '12',
 'cats': '13',
 'panthers': '13',
 'bolts': '14',
 'caps': '15',
 'hawks': '16',
 'wings': '17',
 'preds': '18',
 'blues': '19',
 'flames': '20',
 'avs': '21',
 'oilers': '22',
 'canucks': '23',
 'nooks': '23',
 'nucks': '23',
 'ducks': '24',
 'stars': '25',
 'kings': '26',
 'yotes': '53',
 'sharks': '28',
 'jackets': '29',
 'wild': '30',
 #bunch of non active teams
 'jets': '52',
 'knights': '54'
}

players = 'http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018'
goalies = 'http://www.nhl.com/stats/rest/goalies?isAggregate=false&reportType=goalie_basic&isGame=false&reportName=goaliesummary&sort=[{%22property%22:%22wins%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018'


respPlayers = requests.get(players).json()
respGoalies = requests.get(goalies).json()

def get_standings_info(division):
	output = ''
	json = requests.get('https://statsapi.web.nhl.com/api/v1/standings?season=20172018').json()
	divisionNum = divisions_dictionary[division]
	listOfTeams = json['records'][int(divisionNum)]['teamRecords']
	for x in range(0, len(listOfTeams)):
		output += (str(x+ 1) + ': ')
		output += str(listOfTeams[x]['team']['name'])
		output += ' '

	return output


def get_ppg_info(team_name):
	json = get_team_info(team_name)
	ppg = json['stats'][0]['splits'][0]['stat']['powerPlayGoals']
	team = json['stats'][0]['splits'][0]['team']['name']
	return(str(team)+' have '+str(round(ppg))+' power play goals.')

def get_pk_info(team_name):
	json = get_team_info(team_name)
	pkPercent = json['stats'][0]['splits'][0]['stat']['penaltyKillPercentage']
	pkRank = json['stats'][1]['splits'][0]['stat']['penaltyKillPercentage']
	team = json['stats'][0]['splits'][0]['team']['name']
	return(str(team)+' penalty kill: '+str(pkPercent)+'%, '+str(pkRank)+' in the league')

def get_pp_info(team_name):
	json = get_team_info(team_name)
	ppPercent = json['stats'][0]['splits'][0]['stat']['powerPlayPercentage']
	ppRank = json['stats'][1]['splits'][0]['stat']['powerPlayPercentage']
	team = json['stats'][0]['splits'][0]['team']['name']
	return(str(team)+' powerplay: '+str(ppPercent)+'%, '+str(ppRank)+' in the league')


def get_record(team_name):
	json = get_team_info(team_name)
	gp =  json['stats'][0]['splits'][0]['stat']['gamesPlayed']
	w = json['stats'][0]['splits'][0]['stat']['wins']
	l = json['stats'][0]['splits'][0]['stat']['losses']
	ot = json['stats'][0]['splits'][0]['stat']['ot']
	team = json['stats'][0]['splits'][0]['team']['name']
	return(str(team)+': '+str(w)+'-'+str(l)+'-'+str(ot))

def get_team_info(team_name):
	url = 'https://statsapi.web.nhl.com/api/v1/teams/'+teams_dictionary[team_name]+'/stats'
	return requests.get(url).json()


def get_mugshot(player_name):

	for x in range(0, len(respPlayers['data'])):
		if respPlayers['data'][x]['playerLastName'].lower() == player_name.lower():
			return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(respPlayers['data'][x]['playerId']) + '.jpg')

	for x in range(0, len(respGoalies['data'])):
		if respGoalies['data'][x]['playerLastName'].lower() == player_name.lower():
			return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(respGoalies['data'][x]['playerId']) + '.jpg')

def get_todays_game_from(team_name):
	date_string = year + '-' + month + '-' + day
	URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate='+date_string+'&site=en_nhl&teamId='+teams_dictionary[team_name]
	resp = requests.get(URL).text
	return json.loads(resp)['dates'][0]['games'][0]

def get_live_data(team_name):
    game_json = get_todays_game_from(team_name)
    live_feed_url = game_json["link"]
    URL =  "https://statsapi.web.nhl.com" + live_feed_url
    resp = requests.get(URL).text
    return json.loads(resp)['liveData']

def get_live_boxscore(team_name):
    game_json = get_todays_game_from(team_name)
    live_feed_url = game_json["link"]
    URL =  "https://statsapi.web.nhl.com" + live_feed_url
    resp = requests.get(URL).text
    return json.loads(resp)['liveData']['boxscore']

def get_linescore_from(team_name):
    date_string = year + '-' + month + '-' + day
    URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate='+date_string+'&expand=schedule.linescore&site=en_nhl&teamId='+teams_dictionary[team_name]
    resp = requests.get(URL).text;
    return json.loads(resp)['dates'][0]['games'][0]['linescore']

def stats(player_name):

	for x in range(0, len(respPlayers['data'])):
		if respPlayers['data'][x]['playerLastName'].lower() == player_name.lower():
			return 'GP: ' + str(respPlayers['data'][x]['gamesPlayed']) + ' G: ' + str(respPlayers['data'][x]['goals']) + ' A: ' + str(respPlayers['data'][x]['assists'])

	for x in range(0, len(respGoalies['data'])):
		if respGoalies['data'][x]['playerLastName'].lower() == player_name.lower():
			return 'GP:' + str(respGoalies['data'][x]['gamesPlayed']) + ' W:' + str(respGoalies['data'][x]['wins']) + ' SV%:' + str(respGoalies['data'][x]['savePctg'])

def get_schedule_for_next_5_days(team_name):
    tomorrow = current_date.get_tomorrow()
    five_days_from_now = current_date.get_five_days_from_now()

    URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=' + year + '-' + tomorrow + '&endDate='+year+'-'+five_days_from_now+'&expand=schedule.teams,schedule.broadcasts,schedule.game.content.media.epg&leaderCategories=&site=en_nhl&teamId='+teams_dictionary[team_name]
    resp = requests.get(URL).text;
    return json.loads(resp)
