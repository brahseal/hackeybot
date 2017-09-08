import requests
from random import randint

def get_doggo(breed):
    if breed == None:
        return get_random_doggo()
    else:
        return get_doggo_by_breed(breed)

def get_random_doggo():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    return response.json()["message"]

def get_doggo_by_breed(breed):
    response = requests.get("https://dog.ceo/api/breed/"+breed+"/images")
    images = response.json()["message"]
    return images[randint(0, len(images) -1)]

def get_all_breeds_name():
    response = requests.get("https://dog.ceo/api/breeds/list")
    breeds_array = response.json()["message"]
    breeds = ', '.join(breeds_array)
    return "The available breeds are: " + breeds
