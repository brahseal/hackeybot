import requests
from . import nhl_data
# import nhl_data

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
    schedule = nhl_data.get_schedule_for_next_5_days(team_name)
    next_game = schedule['dates'][0]['games'][0]
    home_team_id = str(next_game['teams']['home']['team']['id'])

    if home_team_id == nhl_data.teams_dictionary[team_name]:
        opponent = next_game['teams']['away']['team']
    else:
        opponent = next_game['teams']['home']['team']

    when = schedule['dates'][0]['date']
    when_weekday = current_date.get_weekday_from(when)
    venue = next_game['venue']['name']

    return team_name + ' are playing against the ' + opponent['teamName'] + ' on ' + when_weekday + ' at ' + venue

def get_remaining_intermission_time(team_name):
    live_data = nhl_data.get_live_data(team_name)
    linescore = live_data["linescore"]
    intermission_info = linescore["intermissionInfo"]
    is_intermission = intermission_info["inIntermission"]
    if not is_intermission:
        return "The " + team_name + " game is not in intermission"
    else :
        time_left = intermission_info["intermissionTimeRemaining"]
        minutes = time_left%3600/60
        if minutes > 1:
            return "There is " + str(int(minutes)) + " minutes left in " + team_name + " game intermission"
        else:
            return "There is " + str(int(time_left)) + " seconds left in " + team_name + " game intermission"

def get_player_live_stats(team_name, player_name):
    live_boxscore = nhl_data.get_live_boxscore(team_name)
    team_id = int(nhl_data.teams_dictionary[team_name])
    home_team_id = live_boxscore["teams"]["home"]["team"]["id"]
    away_team_id =  live_boxscore["teams"]["away"]["team"]["id"]
    if team_id == home_team_id:
        players_stats = live_boxscore["teams"]["home"]["players"]
    else:
        players_stats = live_boxscore["teams"]["away"]["players"]

    for player in players_stats:
        player_info = players_stats[player]
        person = player_info["person"]
        full_name = person["fullName"]
        splitted_name = full_name.split()
        nickname = splitted_name[-1]
        if nickname == player_name or nickname.lower() == player_name:
            return player_info["stats"]['skaterStats']

def get_time_on_ice(team_name, player_name):
    player_stats = get_player_live_stats(team_name, player_name)
    return player_name.title() + " time on ice today: " + player_stats['timeOnIce']

def get_assists(team_name, player_name):
    player_stats = get_player_live_stats(team_name, player_name)
    if player_stats['assists'] == 1:
        return player_name.title() + " has " + str(player_stats['assists']) + " assist today"
    else:
        return player_name.title() + " has " + str(player_stats['assists']) + " assists today"

def get_goals(team_name, player_name):
    player_stats = get_player_live_stats(team_name, player_name)
    if player_stats['goals'] == 1:
        return player_name.title() + " has " + str(player_stats['goals']) + " goal today"
    else:
        return player_name.title() + " has " + str(player_stats['goals']) + " goals today"

def get_hits(team_name, player_name):
    player_stats = get_player_live_stats(team_name, player_name)
    if player_stats['hits'] == 1:
        return player_name.title() + " has " + str(player_stats['hits']) + " hit today"
    else:
        return player_name.title() + " has " + str(player_stats['hits']) + " hits today"

# Not working rn :(
def get_fw(team_name, player_name):
    player_stats = get_player_live_stats(team_name, player_name)
    if player_stats['faceOffWins'] == 1:
        return player_name.title() + " has " + str(player_stats['faceOffWins']) + " faceoff win today, from " + str(player_stats['faceOffTaken']) + " taken"
    else:
        return player_name.title() + " has " + str(player_stats['faceOffWins']) + " faceoff wins today, from " + str(player_stats['faceOffTaken']) + " taken"

def get_plus_minus(team_name, player_name):
    player_stats = get_player_live_stats(team_name, player_name)
    return player_name.title() + " +/- today: " + str(player_stats['plusMinus'])
