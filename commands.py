from random import randint
from mlb import mlb
from mlb import favorite_team
from hackey import penny
from hackey import doggos
from hackey import grills
from hackey import random_responses
from hackey import hackey
from hackey import meme_gen
from nhl import nhl
from nhl import leafs
from mlb import twitter

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
    "mugshot": mlb.get_mugshot,
    "howdidwescore": mlb.get_how_we_score,
}

nhl_commands = {
    "$show": nhl.get_mugshot,
    "$score": nhl.get_game_score_for,
    "$record": nhl.get_record,
    "$sog": nhl.get_sog,
    "$stats": nhl.stats,
    "$pp": nhl.get_pp,
    "$pk": nhl.get_pk,
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
    "pearce": hackey.pearce,
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
    "smoak": hackey.smoak,
    "lou": leafs.lou,
    "help": hackey.help_me,
    "brad": hackey.brad,
    "annika": hackey.annika,
    "dasit": hackey.dasit,
    "borg": hackey.borg,
    "nitro": hackey.nitro,
    "wew": hackey.wew,
    "pude": hackey.pude,
    "cock": hackey.cock,
    "no": hackey.no,
}

other_commands = {
        "penny": penny.get_random_pic,
        "pennyage": penny.get_penny_age,
        "pennydance": penny.get_penny_dance,

        "doggo": doggos.get_doggo,
        "breeds": doggos.get_all_breeds_name,
        "fap": grills.get_qts,
        

        "dome": twitter.get_last_tweet_from_dome,

        "tip": random_responses.get_shitty_LPT,
        "thought": random_responses.get_thought,
        "joke": random_responses.get_joke,
        "motivation": random_responses.get_motivation_image,
        "quote": random_responses.get_quote,
        "countdown": leafs.get_countdown,
    }
meme_gen_commands = {
    "go2bed": meme_gen.get_meme_bed,
    "hang": meme_gen.get_meme_hang,
    "kill": meme_gen.get_meme_grave,
    "golf": meme_gen.get_meme_golf,
    "poop": meme_gen.get_meme_pooper,
    "trash": meme_gen.get_meme_trash,
    "baby": meme_gen.get_meme_diapers,
    "penbox": meme_gen.get_meme_penbox,
}

def get_message_from_command(cmd, args, player):
    if cmd != None and args != None and player == None:
        if cmd in mlb_commands:
            if cmd == "seasonstats" or cmd == "mugshot":
                return mlb_commands[cmd](favorite_team.short_name,args)
            return mlb_commands[cmd](args)
        if cmd in nhl_commands:
            return nhl_commands[cmd](args)
        if cmd in other_commands:
            return other_commands[cmd](args)
        if cmd in meme_gen_commands:
            print("HERE 1" + cmd)
            return meme_gen_commands[cmd](args)
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
        if cmd in mlb_commands:
            return mlb_commands[cmd](args, player)
        if cmd in meme_gen_commands:
            print("HERE 2" + cmd)
            mugshot = mlb.get_mugshot(args, player)
            return meme_gen_commands[cmd](mugshot)
