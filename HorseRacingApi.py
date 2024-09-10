import http.client
import json

class RaceCardRace:
    id_race:int
    course:str
    date:str
    distance:str
    age:str
    finished:bool
    canceled:bool
    offtime:bool
    def __init__(self, data:dict):
        self.id_race = data["id_race"]
        self.course = data["course"]
        self.date = data["date"]
        self.distance = data["distance"]
        self.age = data["age"]
        self.finished = data["finished"]
        self.canceled = data["canceled"]
        self.offtime = data["offtime"]
    def __str__(self):
        return f"{self.date} {self.course} {self.id_race} {self.distance}"

class RaceResult:
    id_race:int
    course:str
    date:str
    distance:str
    age:str
    finished:bool
    canceled:bool
    offtime:bool
    def __init__(self, data:dict):
        self.id_race = data["id_race"]
        self.course = data["course"]
        self.date = data["date"]
        self.distance = data["distance"]
        self.age = data["age"]
        self.finished = data["finished"]
        self.canceled = data["canceled"]
        self.offtime = data["offtime"]
    def __str__(self):
        return f"{self.date} {self.course} {self.id_race} {self.distance}"

class RaceHorseResult:
    horse:str
    id_horse:int
    jockey:str
    trainer:str
    age:str
    weight:str
    number:int
    non_runner:str
    form:str
    position:str
    distance_beaten:str
    odds:str
    poolData:str
    def __init__(self, data:dict):
        self.horse = data["horse"]
        self.id_horse = data["id_horse"]
        self.jockey = data["jockey"]
        self.trainer = data["trainer"]
        self.age = data["age"]
        self.weight = data["weight"]
        self.number = data["number"]
        self.non_runner = data["non_runner"]
        self.form = data["form"]
        self.position = data["position"]
        self.distance_beaten = data["distance_beaten"]
        self.odds = data["odds"]
        self.poolData = data["poolData"]
    def __str__(self):
        return f"{self.position} {self.horse} {self.id_horse} {self.jockey}"

def get_api_data(hostConnectionString, queryString, headers):
    '''
    Generic Api Get method
    '''
    conn = http.client.HTTPSConnection(hostConnectionString)
    conn.request("GET", queryString, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def get_racecard_info(raceDate):

    headers = {
        'x-rapidapi-key': "e059640a1bmshbe4030be7a88e7ep11168fjsn4580fbf9952c",
        'x-rapidapi-host': "horse-racing-usa.p.rapidapi.com"
    }   

    queryString=f"/racecards?date={raceDate}"

    return get_api_data(hostConnectionString="horse-racing-usa.p.rapidapi.com", queryString=queryString, headers=headers)

def get_finishedrace_info(raceDate):

    headers = {
        'x-rapidapi-key': "e059640a1bmshbe4030be7a88e7ep11168fjsn4580fbf9952c",
        'x-rapidapi-host': "horse-racing-usa.p.rapidapi.com"
    }

    queryString=f"/results?date={raceDate}"

    return get_api_data(hostConnectionString="horse-racing-usa.p.rapidapi.com", queryString=queryString, headers=headers)

def get_raceResult_info(raceId:int):

    headers = {
        'x-rapidapi-key': "e059640a1bmshbe4030be7a88e7ep11168fjsn4580fbf9952c",
        'x-rapidapi-host': "horse-racing-usa.p.rapidapi.com"
    }

    queryString=f"/race/{raceId}"

    return get_api_data(hostConnectionString="horse-racing-usa.p.rapidapi.com", queryString=queryString, headers=headers)

def format_racecard_data(raceCardData):
    listOfRaces = json.loads(raceCardData)
    result = [RaceCardRace(race) for race in listOfRaces]     
    return result

def format_finishedRace_data(raceResultData):
    listOfRaces = json.loads(raceResultData)
    result = [RaceResult(race) for race in listOfRaces]     
    return result

def format_race_data(raceResultData):
    raceResult = json.loads(raceResultData)
    if raceResult["horses"] is not None:
        result = [RaceHorseResult(horse) for horse in raceResult["horses"]]     
        return result


if __name__ == '__main__':
    raceDate = '2024-09-10'
    finishedRaceId = 107022
    x = format_racecard_data(get_racecard_info(raceDate))    
    for i in x:
        print(i)

    print('=========================')
    x = format_finishedRace_data(get_finishedrace_info(raceDate))
    for i in x:
        print(i)

    print('=========================')
    r = get_raceResult_info(i.id_race)
    print(r)
    for h in format_race_data(r):
        print(h)

