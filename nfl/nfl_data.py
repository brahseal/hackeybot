import requests
import json


teams_dictionary = {
 'cardinals': '3800',
 'falcons': '0200',
 'ravens': '0325',
 'bills': '0610',
 'panthers': '0750',
 'bears': '0810',
 'bengals': '0920',
 'browns': '1050',
 'cowboys': '1200',
 'broncos': '1400',
 'lions': '1540',
 'packers': '1800',
 'texans': '2120',
 'colts': '2200',
 'jags': '2250',
 'jaguars': '2250',
 'chiefs': '2310',
 'chargers': '4400',
 'rams': '2510',
 'dolphins': '2700',
 'vikings': '3000',
 'patriots': '3200',
 'saints': '3300',
 'giants': '3410',
 'jets': '3430',
 'raiders': '2520',
 'eagles': '3700',
 'steelers': '3900',
 '49ers': '4500',
 'seahawks': '4600',
 'bucks': '4900',
 'buccaneers': '4900',
 'titans': '2100',
 'redskins': '29',
}


def get_score(team_name):
    data = requests.get('https://feeds.nfl.com/feeds-rs/scores.json').json()
    for x in range(0, len(data['gameScores'])):
        if data['gameScores'][x]['gameSchedule']['homeTeamId'] == teams_dictionary[team_name] or data['gameScores'][x]['gameSchedule']['visitorTeamId'] == teams_dictionary[team_name]:
            return data['gameScores'][x]['gameSchedule']['visitorNickname'] + ' (' + str(data['gameScores'][x]['score']['visitorTeamScore']['pointTotal']) + ') @ ' + data['gameScores'][x]['gameSchedule']['homeNickname'] + ' (' + str(data['gameScores'][x]['score']['homeTeamScore']['pointTotal']) + ')'




