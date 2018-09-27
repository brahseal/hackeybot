import requests
from bs4 import BeautifulSoup

def getURL(meme, fucker):

	if fucker != "mdoublee":

		outputURL =  "http://46.228.199.201/mdoublee/memegen/img_output/" + meme + "_" + fucker + ".png"
		print(outputURL)
		return outputURL
	

	
def get_meme_bed(fucker):
	img = getURL('meme_bed_0', fucker)
	return(img)
	
def get_meme_hang(fucker):
	img = getURL('meme_hang_0', fucker)
	return(img)
	
def get_meme_grave(fucker):
	img = getURL('meme_grave_0', fucker)
	return(img)
	
def get_meme_penbox(fucker):
	img = getURL('meme_penbox_0', fucker)
	return(img)
	
def get_meme_golf(fucker):
	img = getURL('meme_golf_0', fucker)
	return(img)
	
def get_meme_pooper(fucker):
	img = getURL('meme_pooper_0', fucker)
	return(img)
	
def get_meme_trash(fucker):
	img = getURL('meme_trash_0', fucker)
	return(img)
	
def get_meme_diapers(fucker):
	img = getURL('meme_diapers_2', fucker)
	return(img)


