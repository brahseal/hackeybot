import requests
import lxml.html
from pprint import pprint
from sys import exit
import json
import csv
from . import current_date
# import current_date
from datetime import datetime
from datetime import date
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

year = current_date.get_year()
month = current_date.get_month()
day = current_date.get_day()

players = 'https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020'
goalies = 'https://api.nhle.com/stats/rest/en/goalie/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22wins%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22savePct%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=50&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020'


respPlayers = requests.get(players).json()
respGoalies = requests.get(goalies).json()

def update_stats():
    global players
    players = 'https://api.nhle.com/stats/rest/en/skater/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22points%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22goals%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22assists%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=100&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020'
    global goalies
    goalies = 'https://api.nhle.com/stats/rest/en/goalie/summary?isAggregate=false&isGame=false&sort=%5B%7B%22property%22:%22wins%22,%22direction%22:%22DESC%22%7D,%7B%22property%22:%22savePct%22,%22direction%22:%22DESC%22%7D%5D&start=0&limit=50&factCayenneExp=gamesPlayed%3E=1&cayenneExp=gameTypeId=2%20and%20seasonId%3C=20192020%20and%20seasonId%3E=20192020'
    global respPlayers
    respPlayers = requests.get(players).json()
    global respGoalies
    respGoalies = requests.get(goalies).json()

def update_time():
    global year
    year = current_date.get_year()
    global month
    month = current_date.get_month()
    global day
    day = current_date.get_day()

sched.add_interval_job(update_time, hours=6)
sched.add_interval_job(update_stats, hours=1)
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


def get_leader(stat_name):
	leaderJSON = requests.get('http://www.nhl.com/stats/rest/leaders?season=20192020&gameType=2').json()
	if stat_name.lower() == 'points' or stat_name.lower() == 'p':
		return 'Points leader: ' +  str(leaderJSON['skater'][0]['leaders'][0]['fullName']) + ' (' + str(leaderJSON['skater'][0]['leaders'][0]['value']) + ')'
	if stat_name.lower() == 'goals' or stat_name.lower() == 'g':
                return 'Goals leader: ' +  str(leaderJSON['skater'][1]['leaders'][0]['fullName']) + ' (' + str(leaderJSON['skater'][1]['leaders'][0]['value']) + ')'
	if stat_name.lower() == 'assists' or stat_name.lower() == 'a':
                return 'Assists leader: ' +  str(leaderJSON['skater'][2]['leaders'][0]['fullName']) + ' (' + str(leaderJSON['skater'][2]['leaders'][0]['value']) + ')'
	if stat_name.lower() == '+-' or stat_name.lower() == 'pm':
                return 'Assists leader: ' +  str(leaderJSON['skater'][3]['leaders'][0]['fullName']) + ' (' + str(leaderJSON['skater'][3]['leaders'][0]['valueLabel']) + ')'
	if stat_name.lower() == 'gaa' or stat_name.lower() == 'ga':
                return 'Goals against leader: ' +  str(leaderJSON['goalie'][0]['leaders'][0]['fullName']) + ' (' + str(leaderJSON['goalie'][0]['leaders'][0]['valueLabel']) + ')'
	if stat_name.lower() == 'save' or stat_name.lower() == 'sv':
                return 'Save % leader: ' +  str(leaderJSON['goalie'][1]['leaders'][0]['fullName']) + ' (' + str(leaderJSON['goalie'][1]['leaders'][0]['valueLabel']) + ')'


def get_age(player_name):
	for x in range(0, len(respPlayers['data'])):
		if respPlayers['data'][x]['playerLastName'].lower() == player_name.lower():
			age = str(respPlayers['data'][x]['playerBirthDate'])
			birthday = datetime.strptime(age, '%Y-%m-%d')
			return str(respPlayers['data'][x]['playerName']) + ' is ' + str(calculate_age(birthday)) + ' years old.'
	for x in range(0, len(respGoalies['data'])):
		if respGoalies['data'][x]['playerLastName'].lower() == player_name.lower():
			age = str(respGoalies['data'][x]['playerBirthDate'])
			birthday = datetime.strptime(age, '%Y-%m-%d')
			return str(respGoalies['data'][x]['playerName']) + ' is ' + str(calculate_age(birthday)) + ' years old.'

def calculate_age(born):
    	today = date.today()
    	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_shooting_percentage(player_name):

	for x in range(0, len(respPlayers['data'])):
		if respPlayers['data'][x]['playerLastName'].lower() == player_name.lower():
			return str(respPlayers['data'][x]['playerName']) + ' shooting percentage: ' + str(format(respPlayers['data'][x]['shootingPctg'] * 100, '.2f')) + '%'

def get_standings_info(division):
	output = ''
	json = requests.get('https://statsapi.web.nhl.com/api/v1/standings?season=20192020').json()
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

def get_mugshot2(player_name, arg2):
	print('in here')
	for x in range(0, len(respPlayers['data'])):
		if (respPlayers['data'][x]['playerFirstName'].lower() == player_name.lower()) and respPlayers['data'][x]['playerLastName'].lower() == arg2.lower():
			return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(respPlayers['data'][x]['playerId']) + '.jpg')

	for x in range(0, len(respGoalies['data'])):
		if respGoalies['data'][x]['playerFirstName'].lower() == player_name.lower() and respGoalies['data'][x]['playerLastName'].lower() == arg2.lower():
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

def get_all_plays_from(team_name):
    game_json = get_todays_game_from(team_name)
    live_feed_url = game_json["link"]
    URL =  "https://statsapi.web.nhl.com" + live_feed_url
    resp = requests.get(URL).text
    return json.loads(resp)['liveData']['plays']

def stats(player_name):

	for x in range(0, len(respPlayers['data'])):
		if respPlayers['data'][x]['lastName'].lower() == player_name.lower():
			return 'GP:' + str(respPlayers['data'][x]['gamesPlayed']) + '  G:' + str(respPlayers['data'][x]['goals']) + '  A:' + str(respPlayers['data'][x]['assists']) + "  P:" + str(respPlayers['data'][x]['points'])

	for x in range(0, len(respGoalies['data'])):
		if respGoalies['data'][x]['lastName'].lower() == player_name.lower():
			return 'GP:' + str(respGoalies['data'][x]['gamesPlayed']) + ' W:' + str(respGoalies['data'][x]['wins']) + ' SV%:' + str(respGoalies['data'][x]['savePctg'])

def stats2(player_name, arg2):

	for x in range(0, len(respPlayers['data'])):
		if (respPlayers['data'][x]['playerFirstName'].lower() == player_name.lower()) and respPlayers['data'][x]['playerLastName'].lower() == arg2.lower():
			return 'GP:' + str(respPlayers['data'][x]['gamesPlayed']) + '  G:' + str(respPlayers['data'][x]['goals']) + '  A:' + str(respPlayers['data'][x]['assists']) + "  P:" + str(respPlayers['data'][x]['points'])

	for x in range(0, len(respGoalies['data'])):
		if (respGoalies['data'][x]['playerFirstName'].lower() == player_name.lower()) and respGoalies['data'][x]['playerLastName'].lower() == arg2.lower():
			return 'GP:' + str(respGoalies['data'][x]['gamesPlayed']) + ' W:' + str(respGoalies['data'][x]['wins']) + ' SV%:' + str(respGoalies['data'][x]['savePctg'])

def get_schedule_for_next_5_days(team_name):
    tomorrow = current_date.get_tomorrow()
    five_days_from_now = current_date.get_five_days_from_now()

    URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=' + year + '-' + tomorrow + '&endDate='+year+'-'+five_days_from_now+'&expand=schedule.teams,schedule.broadcasts,schedule.game.content.media.epg&leaderCategories=&site=en_nhl&teamId='+teams_dictionary[team_name]
    resp = requests.get(URL).text;
    return json.loads(resp)
