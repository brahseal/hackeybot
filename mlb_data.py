import mlbgame
import helper
import time

year = helper.convert_str(time.strftime("%Y"))
month = helper.convert_str(time.strftime("%m"))
day = helper.convert_str(time.strftime("%d"))
hour = helper.convert_str(time.strftime("%H"))

#rewing the day if it's not past 11 a.m (need to check if month is turning)
if hour < 11:
    day -= 1

teams_dictionary = {'cubs': "Cubs", 'yankees': "Yankees", 'redsox': "Red Sox",
                    'mets': "Mets", 'indians': "Indians", 'giants': "Giants",
                    'angels': "Angels", 'dodgers': "Dodgers", 'pirates': "Pirates",
                    'astros': "Astros", 'jays': "Blue Jays", 'bluejays': "Blue Jays",
                    'cards': "Cardinals", 'as': "Athletics", 'athletics': "Athletics",
                    'os': "Orioles", 'orioles': "Orioles", 'rangers': 'Rangers', 'twins': "Twins",
                    'rockies': "Rockies", 'phillies': "Phillies", 'tigers': "Tigers",
                    'rays': "Rays", 'braves': "Braves", 'dbacks': "Diamondbacks",
                    'diamondbacks': "Diamondbacks", 'royals': "Royals", 'brewers': "Brewers",
                    'whitesox': "White Sox", 'reds': "Reds", 'marlins': "Marlins",
                    'padres': "Padres", 'nats': "Nationals", 'mariners': "Mariners"}

def get_all_game_scores():
    games = mlbgame.day(year, month, day)
    games_list = []
    for game in games:
        games_list.append(str(game))

    return (" ".join(games_list))

def get_todays_game( team_name ):
    team = teams_dictionary[team_name]
    game = mlbgame.day(year, month, day, home=team, away=team)
    if game:
        return(game[0])
    else:
        return None

def get_game_overview_xml( team_name ):
    game = get_todays_game(team_name)
    overview = mlbgame.data.get_overview(game.game_id)
    return overview

def get_game_overview_dict( team_name ):
    game = get_todays_game(team_name)
    overview = mlbgame.game.overview(game.game_id)
    return overview

def get_game_status( team_name ):
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
