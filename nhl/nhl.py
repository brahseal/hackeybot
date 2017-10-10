import requests
from . import nhl_data

def stats(player_name):
    return nhl_data.stats(player_name)

def get_mugshot(player_name):
    return nhl_data.get_mugshot(player_name)

def get_game_score_for(team_name):
    game = nhl_data.get_todays_game_from(team_name)

    away_team = game['teams']['away']['team']['name']
    away_team_score = str(game['teams']['away']['score'])

    home_team = game['teams']['home']['team']['name']
    home_team_score = str(game['teams']['home']['score'])

    return home_team + " " + home_team_score + " - " + away_team + " " + away_team_score


def is_team_at_home(team_name):
    game = nhl_data.get_todays_game_from(team_name)

    home_team_id = str(game['teams']['home']['team']['id'])
    return home_team_id == nhl_data.teams_dictionary[team_name]

def get_team_record(team_name):
    game = nhl_data.get_todays_game_from(team_name)
    if is_team_at_home(team_name):
        team_wins = str(game['teams']['home']['leagueRecord']['wins'])
        team_losses = str(game['teams']['home']['leagueRecord']['losses'])
        team_ot_loss = str(game['teams']['home']['leagueRecord']['ot'])
        return team_name + " are " + team_wins + "-" + team_losses + "-" + team_ot_loss
    else:
        team_wins = str(game['teams']['away']['leagueRecord']['wins'])
        team_losses = str(game['teams']['away']['leagueRecord']['losses'])
        team_ot_loss = str(game['teams']['home']['leagueRecord']['ot'])
        return team_name + " are " + team_wins + "-" + team_losses + "-" + team_ot_loss

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
