from __future__ import print_function
import time
import sys, os
import mlbgame
from helper import helper
import xml.etree.ElementTree as ET
import mlb.mlb_data as mlb_data
import mlb.favorite_team as favorite_team

def get_conditions(team_name):
    return(mlb_data.get_weather(team_name))

def get_standings(division):
    return(mlb_data.get_standings(division))

def is_team_at_home( team_name ):
    game = mlb_data.get_todays_game(team_name)
    if game.home_team == mlb_data.teams_dictionary[team_name]:
        return True
    else:
        return False

def is_team_playing( team_name ):
    game = mlb_data.get_todays_game(team_name)
    print(game)
    return game != None

#!score team_name command return
def get_team_score( team_name ):
    print(mlb_data.get_score(team_name))
    return mlb_data.get_score(team_name)
    


    

def get_current_batter( team_name ):
    #check other possible statuses
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME":
        return "Game hasn't started yet"

    xml = mlb_data.get_game_overview_xml(team_name)
    tree = ET.parse(xml)
    root = tree.getroot()

    for data in root:
        for current_batter in data.iter('current_batter'):
            player_id = current_batter.attrib['id']
            current_batter = "http://gdx.mlb.com/images/gameday/mugshots/mlb/"+player_id+".jpg " + current_batter.attrib['first_name'] + " " + current_batter.attrib['last_name'] + " is batting."
            return current_batter

def get_team_record( team_name ):
    return mlb_data.get_record(team_name)

def get_pitching_line( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME":
        return "Game hasn't started yet"

    game_stats = mlb_data.get_player_stats(team_name)
    if is_team_at_home(team_name):
        pitcher_stats = game_stats['home_pitching'][0]
    else:
        pitcher_stats = game_stats['away_pitching'][0]

    pitcher_outs = int(pitcher_stats['out'])
    pitcher_er = pitcher_stats['er']
    pitcher_r = pitcher_stats['r']
    pitcher_hits = pitcher_stats['h']
    pitcher_so = pitcher_stats['so']
    pitcher_walks = pitcher_stats['bb']
    pitcher_np = pitcher_stats['np']
    pitcher_strikes = pitcher_stats['s']
    pitcher_wins = pitcher_stats['w']
    pitcher_losses = pitcher_stats['l']
    pitcher_era = pitcher_stats['era']
    pitcher_id = pitcher_stats['id']

    if pitcher_outs % 3 == 1:
        innings_pitched = str(int((pitcher_outs -1) / 3))
        IP = innings_pitched + ".1"
    elif pitcher_outs % 3 == 2:
        innings_pitched = str(int((pitcher_outs -2) / 3))
        IP = innings_pitched + ".2"
    else:
        IP = str(pitcher_outs/3) + ""

    message = "http://gdx.mlb.com/images/gameday/mugshots/mlb/"+pitcher_id+".jpg " + pitcher_stats['name'] + " pitching line: " + IP + "IP " + pitcher_er + "ER " + pitcher_hits +"H " + pitcher_so + "SO " + pitcher_walks + "BB " + pitcher_strikes + "-" + pitcher_np + " strikes/pitches "
    return message

def get_game_time( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "IN_PROGRESS":
        return "Game is in progress. Hurry up, you can still catch it"
    overview_dict = mlb_data.get_game_overview_dict(team_name)
    start_time = overview_dict['time']
    time_zone = overview_dict['time_zone']
    am_pm = overview_dict['ampm']
    message = "Today's " + mlb_data.teams_dictionary[team_name] + " game will start at " + start_time + am_pm + " " + time_zone
    return message

def get_last_ab( team_name ):
    overview = mlb_data.get_game_overview_dict(team_name)
    current_inning = overview['inning']
    inning_state = overview['inning_state'].lower()
    events = mlb_data.get_game_events(team_name)
    last_event = events[current_inning][inning_state]
    if last_event == None:
        return "Nothing happened in this inning yet"
    return str(last_event[-1])

def get_ondeck_batter( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME":
        return "Game hasn't start yet"

    xml = mlb_data.get_game_overview_xml(team_name)
    tree = ET.parse(xml)
    root = tree.getroot()

    for data in root:
        for current_ondeck in data.iter('current_ondeck'):
            player_id = current_ondeck.attrib['id']
            current_ondeck = 'http://gdx.mlb.com/images/gameday/mugshots/mlb/'+player_id+'.jpg ' + current_ondeck.attrib['first_name'] + " " + current_ondeck.attrib['last_name'] + " is on deck "
            return current_ondeck

def get_inhole_batter( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME":
        return "Game hasn't started yet"

    xml = mlb_data.get_game_overview_xml(team_name)
    tree = ET.parse(xml)
    root = tree.getroot()

    for data in root:
        print(data)
        for current_inhole in data.iter('current_inhole'):
            player_id = current_inhole.attrib['id']
            current_inhole = ' http://gdx.mlb.com/images/gameday/mugshots/mlb/'+player_id+'.jpg '+ current_inhole.attrib['first_name'] + " " + current_inhole.attrib['last_name'] + " is in the hole "
            return current_inhole

def get_due_up_batters( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME":
        return "Game hasn't started yet"
    return get_current_batter(team_name) + " " + get_ondeck_batter(team_name) + " " + get_inhole_batter(team_name)

def get_starting_pitcher( team_name ):
    game_status = mlb_data.get_game_status(team_name)
    if game_status == "PRE_GAME" or game_status == "IMMEDIATE_PREGAME":
        xml = mlb_data.get_game_overview_xml(team_name)
        tree = ET.parse(xml)
        root = tree.getroot()

        if is_team_at_home(team_name):
            for data in root:
                for starting_pitcher in data.iter('home_probable_pitcher'):
                    starting_pitcher_id = starting_pitcher.attrib['id']
                    starting_pitcher = ' http://gdx.mlb.com/images/gameday/mugshots/mlb/'+starting_pitcher_id+'.jpg '+ starting_pitcher.attrib['first_name'] + " " + starting_pitcher.attrib['last_name'] + " is starting today for the " + team_name
                    return starting_pitcher
        else:
            for data in root:

                for starting_pitcher in data.iter('away_probable_pitcher'):
                    starting_pitcher_id = starting_pitcher.attrib['id']
                    starting_pitcher = ' http://gdx.mlb.com/images/gameday/mugshots/mlb/'+starting_pitcher_id+'.jpg '+ starting_pitcher.attrib['first_name'] + " " + starting_pitcher.attrib['last_name'] + " is starting today for the " + team_name
                    return starting_pitcher
    elif game_status == "IN_PROGRESS":
        return mlb_data.teams_dictionary[team_name] + " game started already. The starting pitcher was " + get_pitching_line(team_name)
    else:
        return mlb_data.teams_dictionary[team_name] + " game is over. The starting pitcher line was" + get_pitching_line(team_name)


def get_player_stats( team_name, player_name ):
    game_stats = mlb_data.get_player_stats(team_name)

    if is_team_at_home(team_name):
        team_player_stats = game_stats['home_batting']
    else:
        team_player_stats = game_stats['away_batting']

    for player in team_player_stats:
        if player['name'].lower() == player_name:

            player_at_bats = player['ab']
            player_hits = player['h']
            player_walks = player['bb']
            player_home_runs = player['hr']
            player_rbi = player['rbi']
            player_lob = player['lob']

            message = player['name'] + " is " + player_hits + "-" + player_at_bats + " today "
            if int(player_walks) == 1:
                message += "with a walk "
            elif int(player_walks) > 1:
                message += "with " + player_walks + " walks "
            if int(player_home_runs) == 1:
                message += "He's also hit a home run "
            elif int(player_home_runs) > 1:
                message += "He's also hit " + player_home_runs + " homers "
            if int(player_rbi) == 1:
                message += "and has one RBI "
            elif int(player_rbi) > 1:
                message += "and has "+ player_rbi + " RBI's "
            if int(player_lob) >= 3:
                message += "also he stranded " + player_lob + " players on base"

            return message
    return "Sorry, i don't recognize that name, please use the name on the player uniform, or make sure he's in today's lineup for the " + team_name

def get_player_season_stats( team_name, player_name ):
    game_stats = mlb_data.get_player_stats(team_name)
    if is_team_at_home(team_name):
        team_player_stats = game_stats['home_batting']
    else:
        team_player_stats = game_stats['away_batting']

    for player in team_player_stats:
        if player['name'].lower() == player_name:

            player_id = player['id']
            player_name = player['name_display_first_last']
            player_avg = player['avg']
            player_obp = player['obp']
            player_slg = player['slg']
            player_ops = player['ops']

            message = ' http://gdx.mlb.com/images/gameday/mugshots/mlb/'+player_id+'.jpg ' + player_name + " " + player_avg + " AVG | " + player_obp + " OBP | " + player_slg + " SLG | " + player_ops + " OPS"
            return message

    return "Sorry, i don't recognize that name, please use the name on the player uniform, or make sure he plays for the " + team_name



def get_mugshot(player_name):
    return mlb_data.get_mugshot(player_name)

def get_how_we_score( team_name ):
    overview = mlb_data.get_game_overview_dict(team_name)

    current_inning = overview['inning']
    inning_state = overview['inning_state'].lower()
    scoring_plays = []
    events = mlb_data.get_game_events(team_name)
    # print(events['1']['top'][0])
    if is_team_at_home(team_name):
        for inning in events:
            for event in events[inning]['bottom']:
                if 'scores' in event.des:
                    scoring_plays.append(event.des)
    else:
        for inning in events:
            for event in events[inning]['top']:
                if 'scores' in event.des or 'homers' in event.des:
                    scoring_plays.append(event.des)

    last_3_scoring_plays = scoring_plays[-1:]
    return ''.join(last_3_scoring_plays)
