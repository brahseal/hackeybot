import mlbgame
from helper import current_time
from datetime import datetime
from apscheduler.scheduler import Scheduler
import sys

import requests

# Start the scheduler
sched = Scheduler()
sched.start()

year = current_time.get_year()
month = current_time.get_month()
day = current_time.get_day()

def update_time():
    global year
    year = current_time.get_year()
    global month
    month = current_time.get_month()
    global day
    day = current_time.get_day()

sched.add_interval_job(update_time, hours=1)


teams_dictionary = {
 'orioles': '110',
 'red sox': '111',
 'redsox': '111',
 'white sox': '145',
 'whitesox': '145',
 'indians': '114',
 'tigers': '116',
 'astros': '117',
 'royals': '118',
 'angels': '108',
 'twins': '142',
 'yankees': '147',
 'athletics': '133',
 'mariners': '136',
 'rays': '139',
 'rangers': '140',
 'jays': '141',
 'diamondbacks': '109',
 'dbacks': '109',
 'd-backs': '109',
 'sneks': '109',
 'braves': '144',
 'cubs': '112',
 'reds': '113',
 'rockies': '115',
 'dodgers': '119',
 'doyers': '119',
 'marlins': '146',
 'brewers': '158',
 'mets': '121',
 'phillies': '143',
 'pirates': '134',
 'padres': '135',
 'giants': '137',
 'cardinals': '138',
 'cards': '138',
 'nationals': '120',
 'nats': '120'
}

division_dictionary = {
  'alw': '200',
  'ale': '201',
  'alc': '202',
  'nlw': '203',
  'nle': '204',
  'nlc': '205'
}

standings = requests.get('https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season=2019&standingsTypes=regularSeason').json()
team_standings = {}

def get_score(team_name):
    if team_name in teams_dictionary:
        url = 'https://statsapi.mlb.com/api/v1/schedule?sportId=1,51&date='+str(datetime.now().date())+'&teamId='+teams_dictionary[team_name]
        print(url)
        json = requests.get(url).json()
        url2 = 'https://statsapi.mlb.com/api/v1.1/game/'+str(get_game_id(team_name))+'/feed/live'
        json2 = requests.get(url2).json()
        if int(json['dates'][0]['totalGames']) > 0:

            awayTeam = json['dates'][0]['games'][0]['teams']['away']['team']['id']
            homeTeam = json['dates'][0]['games'][0]['teams']['home']['team']['id']
            if json['dates'][0]['games'][0]['status']['abstractGameState'] == 'Final':
                awayScore = json['dates'][0]['games'][0]['teams']['away']['score']
                homeScore = json['dates'][0]['games'][0]['teams']['home']['score']
                return get_short_name(awayTeam)+' ('+str(awayScore)+') @ '+get_short_name(homeTeam)+' ('+str(homeScore)+') [Final]'
            if int(json['dates'][0]['totalGamesInProgress']) == 0:
                time = str(json2['gameData']['datetime']['time']) + ' ' + str(json2['gameData']['datetime']['ampm'])
                return get_short_name(awayTeam)+' @ '+get_short_name(homeTeam)+' '+ time

            else:
                awayScore = json['dates'][0]['games'][0]['teams']['away']['score']
                homeScore = json['dates'][0]['games'][0]['teams']['home']['score']
                inning = json2['liveData']['linescore']['currentInningOrdinal']
                if json2['liveData']['linescore']['isTopInning']:
                    inningType = 'Top'
                else:
                    inningType = 'Bottom'
                return get_short_name(awayTeam)+' ('+str(awayScore)+') @ '+get_short_name(homeTeam)+' ('+str(homeScore)+') [' + inningType + ' ' + inning + ']'

        else:
            return 'No '+team_name+' game today!'

def get_short_name(team_id):
	json = requests.get('https://statsapi.mlb.com/api/v1/teams/'+str(team_id)).json()
	return json['teams'][0]['teamName']

def get_stats_data(team_name):
    url = 'https://statsapi.mlb.com/api/v1/schedule?sportId=1,51&date='+str(datetime.now().date())+'&teamId='+teams_dictionary[team_name]
    json = requests.get(url).json()
    print(json)
    return json

def get_content_data(team_name):
    url = 'https://statsapi.mlb.com/api/v1/schedule?sportId=1,51&date='+str(datetime.now().date())+'&teamId='+teams_dictionary[team_name]
    json = requests.get(url).json()
    print(json)
    content_url = json['dates'][0]['games'][0]['content']['link']
    print(content_url)
    return requests.get('https://statsapi.mlb.com'+content_url).json()

def get_mugshot(player_name):
	url = 'http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=mlb&active_sw=%27Y%27&name_part=%27'+player_name+'%25%27'
	json = requests.get(url).json()
	if int(json['search_player_all']['queryResults']['totalSize']) == 1:
		id = json['search_player_all']['queryResults']['row']['player_id']
	else:
		id = json['search_player_all']['queryResults']['row'][0]['player_id']
	return 'http://gdx.mlb.com/images/gameday/mugshots/mlb/'+id+'.jpg'

def update_records():
    standings = requests.get('https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season=2019&standingsTypes=regularSeason').json()
    for i in range(6):
        for j in range(5):
            id = standings['records'][i]['teamRecords'][j]['team']['id']
            record = str(standings['records'][i]['teamRecords'][j]['team']['name']) + ': ' + str(standings['records'][i]['teamRecords'][j]['wins']) + '-' + str(standings['records'][i]['teamRecords'][j]['losses'])
            team_standings[id] = record
update_records()
sched.add_interval_job(update_records, hours=1)

def get_standings(division):
    output = ''
    for i in range(6):
        if standings['records'][i]['division']['id'] == int(division_dictionary[division]):
            for j in range(5):
                output += (str(j + 1) + ':' + str(standings['records'][i]['teamRecords'][j]['team']['name']) + ' ')
    return output

def get_record(team_name):
    return team_standings[int(teams_dictionary[team_name])]


def get_game_id(team_name):
    data = requests.get('https://statsapi.mlb.com/api/v1/schedule?sportId=1,51&date='+str(datetime.now().date())+'&teamId='+teams_dictionary[team_name]).json()
    if data['dates'][0]['totalGames'] > 0:
        return data['dates'][0]['games'][0]['gamePk']

def get_weather(team_name):
    data = requests.get('https://statsapi.mlb.com/api/v1.1/game/' + str(get_game_id(team_name)) + '/feed/live').json()
    condition = data['gameData']['weather']['condition']
    temp = data['gameData']['weather']['temp']
    return (condition + ', ' + temp + ' degrees')

def get_todays_game( team_name ):
    team = teams_dictionary[team_name]
    game = mlbgame.day(year, month, day, home=team, away=team)
    print(game[0])
    if game:
        return(game[0])
    else:
        return None

def get_game_overview_xml( team_name ):
    print(year)
    game = get_todays_game(team_name)
    overview = mlbgame.data.get_overview(game.game_id)
    return overview

def get_game_overview_dict( team_name ):
    print(year)
    game = get_todays_game(team_name)
    overview = mlbgame.game.overview(game.game_id)
    return overview

def get_game_status( team_name ):
    print(year)
    game = get_todays_game(team_name)
    return game.game_status

def get_player_stats( team_name ):
    game = get_todays_game(team_name)
    player_stats = mlbgame.stats.player_stats(game.game_id)
    return player_stats

def get_game_events( team_name ):
    game = get_todays_game(team_name)
    if game != None:
        events = mlbgame.game_events(game.game_id)
        return events
    else:
        return("Looks like there's no " + team_name + " game today")
