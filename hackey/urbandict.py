from random import randint
import requests
import json

def get_random_definition_from(word):
    url = 'http://api.urbandictionary.com/v0/define?term='+word
    response = requests.get(url).json()
    definition_list = response['list']
    if not definition_list:
        return  "Sorry, i couldn't find any definition for that word"
    definition = definition_list[randint(0, len(definition_list)-1)]['definition']
    if len(definition) > 180:
        return "The definition for "+ word+" is too long, i don't want to flood the chat"
    return definition
