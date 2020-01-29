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


def update_time():
    global year
    year = current_date.get_year()
    global month
    month = current_date.get_month()
    global day
    day = current_date.get_day()


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

id_dict = {}
pos_dict = {}


def update_ids():
    for x in teams_dictionary:
        leaderJSON = requests.get('https://statsapi.web.nhl.com/api/v1/teams/' + teams_dictionary[x] + '/roster').json()
        for team in range(0,len(leaderJSON['roster'])):
            id_dict[leaderJSON['roster'][team]['person']['fullName'].lower()] = leaderJSON['roster'][team]['person']['id']
            id_dict[leaderJSON['roster'][team]['person']['fullName'].split(' ', 1)[-1].lower()] = leaderJSON['roster'][team]['person']['id']
            pos_dict[leaderJSON['roster'][team]['person']['fullName'].lower()] = leaderJSON['roster'][team]['position']['code']
            pos_dict[leaderJSON['roster'][team]['person']['fullName'].split(' ', 1)[-1].lower()] = leaderJSON['roster'][team]['position']['code']



sched.add_interval_job(update_time, hours=6)
sched.add_interval_job(update_ids, hours=6)
update_ids()


def get_leader(stat_name):
	assists = requests.get('https://api.nhle.com/stats/rest/en/leaders/skaters/assists?cayenneExp=season=20192020').json()
	points = requests.get('https://api.nhle.com/stats/rest/en/leaders/skaters/points?cayenneExp=season=20192020').json()
	goals = requests.get('https://api.nhle.com/stats/rest/en/leaders/skaters/goals?cayenneExp=season=20192020').json()
	gaa = requests.get('https://api.nhle.com/stats/rest/en/leaders/goalies/gaa?cayenneExp=season=20192020').json()
	save = requests.get('https://api.nhle.com/stats/rest/en/leaders/goalies/savePctg?cayenneExp=season=20192020').json()
	if stat_name.lower() == 'points' or stat_name.lower() == 'p':
		return 'Points leader: ' +  str(points['data'][0]['player']['fullName']) + ' (' + str(points['data'][0]['points']) + ')'
	if stat_name.lower() == 'goals' or stat_name.lower() == 'g':
		return 'Goals leader: ' +  str(goals['data'][0]['player']['fullName']) + ' (' + str(goals['data'][0]['goals']) + ')'
	if stat_name.lower() == 'assists' or stat_name.lower() == 'a':
		return 'Assists leader: ' +  str(assists['data'][0]['player']['fullName']) + ' (' + str(assists['data'][0]['assists']) + ')'
	if stat_name.lower() == 'gaa' or stat_name.lower() == 'ga':
		return 'Goals against leader: ' +  str(gaa['data'][0]['player']['fullName']) + ' (' + str(gaa['data'][0]['gaa']) + ')'
	if stat_name.lower() == 'save' or stat_name.lower() == 'sv':
		return 'Save % leader: ' +  str(save['data'][0]['player']['fullName']) + ' (' + str(save['data'][0]['savePctg']) + ')'


def get_age(player_name):
	player = requests.get('https://statsapi.web.nhl.com/api/v1/people/' + str(id_dict[player_name.lower()])).json()
	bday = player['people'][0]['birthDate']
	birthday = datetime.strptime(bday, '%Y-%m-%d')
	return player['people'][0]['fullName'] + ' is ' + str(calculate_age(birthday)) + ' years old.'

def calculate_age(born):
    	today = date.today()
    	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_shooting_percentage(player_name):
	data = requests.get('https://statsapi.web.nhl.com/api/v1/people/' + str(id_dict[player_name.lower()]) + '/stats?stats=statsSingleSeason&season=20192020').json()
	value = data['stats'][0]['splits'][0]['stat']['shotPct']
	player = requests.get('https://statsapi.web.nhl.com/api/v1/people/' + str(id_dict[player_name.lower()])).json()
	return player['people'][0]['fullName'] + ' shooting percentage: ' + str(value) + '%'

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
	return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(id_dict[player_name.lower()]) + '.jpg')

def get_mugshot2(player_name, arg2):
	print('in here')
	return('https://nhl.bamcontent.com/images/headshots/current/168x168/' + str(id_dict[player_name.lower() + ' ' + arg2.lower()]) + '.jpg')

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
    data = requests.get('https://statsapi.web.nhl.com/api/v1/people/' + str(id_dict[player_name.lower()]) + '/stats?stats=statsSingleSeason&season=20192020').json()
    if pos_dict[player_name.lower()] == 'G':
        return 'GP:' + str(data['stats'][0]['splits'][0]['stat']['games']) + ' W:' + str(data['stats'][0]['splits'][0]['stat']['wins']) + ' SV%:' + str(round(data['stats'][0]['splits'][0]['stat']['savePercentage'], 2)) + ' GAA:' + str(round(data['stats'][0]['splits'][0]['stat']['goalAgainstAverage'], 2))
    else:
        return 'GP:' + str(data['stats'][0]['splits'][0]['stat']['games']) + '  G:' + str(data['stats'][0]['splits'][0]['stat']['goals']) + '  A:' + str(data['stats'][0]['splits'][0]['stat']['assists']) + "  P:" + str(data['stats'][0]['splits'][0]['stat']['points'])

def stats2(player_name, arg2):
    data = requests.get('https://statsapi.web.nhl.com/api/v1/people/' + str(id_dict[player_name.lower() + " " + arg2.lower()]) + '/stats?stats=statsSingleSeason&season=20192020').json()
    if pos_dict[player_name.lower() + " " + arg2.lower()] == 'G':
        return 'GP:' + str(data['stats'][0]['splits'][0]['stat']['games']) + ' W:' + str(data['stats'][0]['splits'][0]['stat']['wins']) + ' SV%:' + str(round(data['stats'][0]['splits'][0]['stat']['savePercentage'], 2)) + ' GAA:' + str(round(data['stats'][0]['splits'][0]['stat']['goalAgainstAverage'], 2))
    else:
        return 'GP:' + str(data['stats'][0]['splits'][0]['stat']['games']) + '  G:' + str(data['stats'][0]['splits'][0]['stat']['goals']) + '  A:' + str(data['stats'][0]['splits'][0]['stat']['assists']) + "  P:" + str(data['stats'][0]['splits'][0]['stat']['points'])

def get_schedule_for_next_5_days(team_name):
    tomorrow = current_date.get_tomorrow()
    five_days_from_now = current_date.get_five_days_from_now()

    URL = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=' + year + '-' + tomorrow + '&endDate='+year+'-'+five_days_from_now+'&expand=schedule.teams,schedule.broadcasts,schedule.game.content.media.epg&leaderCategories=&site=en_nhl&teamId='+teams_dictionary[team_name]
    resp = requests.get(URL).text;
    return json.loads(resp)
