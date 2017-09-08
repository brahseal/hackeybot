from urllib.request import urlopen

def get_avi(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=basic_getavi_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_bed(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_bed_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_hang(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_hang_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_grave(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_grave_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_penbox(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_penbox_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_golf(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_golf_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_pooper(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_pooper_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_trash(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_trash_0&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]

def get_meme_diapers(fucker):
    geturl = "http://46.228.199.201/mdoublee/memegen2/php/wrapper_oldmemegen.php?selectedscript=meme_diapers_2&fucker="+fucker
    memeurl = urlopen(geturl).read()
    string_url = str(memeurl.strip())
    return string_url.split("'", 2)[1]
