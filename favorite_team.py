import mlbgame
import mlb
import mlb_data
import xml.etree.ElementTree as ET
short_name = "jays"
full_name = "BlueJays"

def set_favorite_team(team_name):
    self.short_name = team_name
    self.full_name = mlb_data.teams_dictionary[team_name]

def is_favorite_team_at_home():
    return mlb.is_team_at_home(full_name)

def is_favorite_team_batting():
    overview = mlb_data.get_game_overview_dict(full_name)
    inning_state = overview['inning_state']
    if inning_state == 'Top' and is_favorite_team_at_home():
        return False
    elif inning_state == 'Top' and not jays_at_home_eh:
        return False
    elif is_favorite_team_at_home():
        return True

def is_favorite_team_playing_today():
    game = mlb_data.get_todays_game(full_name)
    return game != None
