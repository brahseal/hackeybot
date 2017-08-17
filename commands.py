from random import randint
import mlb
import favorite_team
import penny
import doggos
import grills
import twitter
import random_responses
import hackey
import leafs

mlb_commands = {

    "score": mlb.get_team_score,
    "pitching": mlb.get_current_pitcher,
    "batting": mlb.get_current_batter,
    "line": mlb.get_pitching_line,
    "record": mlb.get_team_record,
    "time": mlb.get_game_time,
    "lastab": mlb.get_last_ab,
    "ondeck": mlb.get_ondeck_batter,
    "inhole": mlb.get_inhole_batter,
    "dueup": mlb.get_due_up_batters,
    "starting": mlb.get_starting_pitcher,
    "stats": mlb.get_player_stats,
    "seasonstats": mlb.get_player_season_stats,
}

hackey_commands = {
    "wings": hackey.wings,
    "brahseal": hackey.brahseal,
    "avs": hackey.avs,
    "pudge": hackey.pudge,
    "gare": hackey.gare,
    "natty": hackey.natty,
    "mdoublee": hackey.mdoublee,
    "deez": hackey.deez,
    "swishhhhh": hackey.swishhhhh,
    "pond": hackey.pond,
    "zezi": hackey.zezi,
    "tim": hackey.coachtim,
    "kawa": hackey.kawa,
    "evbo": hackey.evbo,
    "gov": hackey.gov,
    "porp": hackey.prop,
    "hash": hackey.hashi,
    "ross": hackey.ross,
    "gif": hackey.jays_gifs,
    "faggot": hackey.faggot,
    "biglenny": hackey.big_lenny,
    "13reasons": hackey.reasons,
    "venn": hackey.venn,
    "ageofconsent": hackey.consent,
    "gibby": hackey.gibbys,
    "shapoo": hackey.shapoo,
    "swing": hackey.swing,
    "ninja": hackey.ninja,
    "moose": hackey.moose,
    "jay": hackey.jay,
    "sens": hackey.sens,
    "nucks": hackey.nucks,
    "don": hackey.don,
}

other_commands = {
        "penny": penny.get_random_pic,
        "pennyage": penny.get_penny_age,
        "pennydance": penny.get_penny_dance,

        "doggo": doggos.get_doggo,
        "breeds": doggos.get_all_breeds_name,
        "fap": grills.get_qts,
        "brazzers": grills.get_brazzers,

        "dome": twitter.get_last_tweet_from_dome,

        "tip": random_responses.get_shitty_LPT,
        "thought": random_responses.get_thought,
        "joke": random_responses.get_joke,
        "motivation": random_responses.get_motivation_image,
        "quote": random_responses.get_quote,
        "countdown": leafs.get_countdown,
    }


def get_message_from_command(cmd, args, player):
    if cmd != None and args != None and player == None:
        if cmd in mlb_commands:
            if cmd == "seasonstats":
                return mlb_commands[cmd](favorite_team.short_name,args)
            return mlb_commands[cmd](args)
        if cmd in other_commands:
            return other_commands[cmd](args)
    elif cmd != None and args == None and player == None:
        if cmd in mlb_commands:
            return mlb_commands[cmd](favorite_team.short_name)
        if cmd in other_commands:
            if cmd == "doggo":
                return other_commands[cmd](None)
            return other_commands[cmd]()
        if cmd in hackey_commands:
            return hackey_commands[cmd][randint(0, len(hackey_commands[cmd])-1)]
    else:
        return mlb_commands[cmd](args, player)
