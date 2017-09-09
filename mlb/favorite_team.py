import mlbgame
import xml.etree.ElementTree as ET

short_name = "jays"
full_name = "BlueJays"

def set_favorite_team(team_name):
    import mlb.mlb_data as mlb_data
    self.short_name = team_name
    self.full_name = mlb_data.teams_dictionary[team_name]

def is_favorite_team_at_home():
    import mlb.mlb as mlb
    return mlb.is_team_at_home(full_name)

def is_favorite_team_batting():
    import mlb.mlb_data as mlb_data
    overview = mlb_data.get_game_overview_dict(full_name)
    inning_state = overview['inning_state']
    if inning_state == 'Top' and is_favorite_team_at_home():
        return False
    elif inning_state == 'Top' and not jays_at_home_eh:
        return False
    elif is_favorite_team_at_home():
        return True

def is_favorite_team_playing_today():
    import mlb.mlb_data as mlb_data
    game = mlb_data.get_todays_game(full_name)
    return game != None
