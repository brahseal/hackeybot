import requests
from . import nhl_data

def get_standings(division):
    return nhl_data.get_standings_info(division)

def get_ppg(team_name):
    return nhl_data.get_ppg_info(team_name)

def get_pk(team_name):
    return nhl_data.get_pk_info(team_name)
 
def get_pp(team_name):
    return nhl_data.get_pp_info(team_name)

def get_record(team_name):
    return nhl_data.get_record(team_name)

def stats(player_name):
    return nhl_data.stats(player_name)

def get_mugshot(player_name):
    return nhl_data.get_mugshot(player_name)

def get_game_score_for(team_name):
    game = nhl_data.get_todays_game_from(team_name.lower())

    away_team = game['teams']['away']['team']['name']
    away_team_score = str(game['teams']['away']['score'])

    home_team = game['teams']['home']['team']['name']
    home_team_score = str(game['teams']['home']['score'])

    return home_team + " " + home_team_score + " - " + away_team + " " + away_team_score


def is_team_at_home(team_name):
    game = nhl_data.get_todays_game_from(team_name)

    home_team_id = str(game['teams']['home']['team']['id'])
    return home_team_id == nhl_data.teams_dictionary[team_name]


def get_sog(team_name):
    linescore = nhl_data.get_linescore_from(team_name)
    if is_team_at_home(team_name):
        sog = str(linescore['teams']['home']['shotsOnGoal'])
        print(sog)
        return 'The ' + team_name + " have " + sog + " shots on goal"
    else:
        sog = str(linescore['teams']['away']['shotsOnGoal'])
        print(sog)
        return 'The ' + team_name + " have " + sog + " shots on goal"

def get_next_game_for(team_name):
    from . import current_date
    print('Called NEXTGAME function')
    schedule = nhl_data.get_schedule_for_next_5_days(team_name)
    next_game = schedule['dates'][0]['games'][0]
    home_team_id = str(next_game['teams']['home']['team']['id'])

    if home_team_id == nhl_data.teams_dictionary[team_name]:
        opponent = next_game['teams']['away']['team']
    else:
        opponent = next_game['teams']['home']['team']

    when = next_game['gameDate'][:10]
    when_weekday = current_date.get_weekday_from(when)
    venue = next_game['venue']['name']

    return team_name + ' are playing against the ' + opponent['teamName'] + ' on ' + when_weekday + ' at ' + venue