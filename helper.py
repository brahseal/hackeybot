import mlbgame

def convert_str(s):
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret

def clear_cache():
    mlbgame.update.clear()
