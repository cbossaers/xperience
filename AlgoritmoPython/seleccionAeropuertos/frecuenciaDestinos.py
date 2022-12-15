import json
import os

def getJson():
    # assign directory
    directory = 'AlgoritmoPython/seleccionAeropuertos/airportDestinations'
    # list of airports we dont want
    listDirectory = list(map(lambda x: x.replace('.json', ''), os.listdir(directory)))
    result = {}
    stradded = ""
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            with open(f, 'r') as file:
                mydata = json.load(file)
           
            for element in mydata["response"]:
                if element["arr_iata"] not in listDirectory : 
                    if result.get(element["arr_iata"]) is None :
                        result.update({element["arr_iata"] : 1})
                        stradded = stradded + " " + element["arr_iata"]
                    else:
                        result.update({element["arr_iata"] : result.get(element["arr_iata"])+1})
    #print("Added" + stradded)
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))
    with open ("./frecuenciaDestinos.json", "w") as res:
        json.dump(result, res, indent = 2)
    
def getNumberOfTravels(number):
    with open ("frecuenciaDestinos.json", "r") as res:
        dic = json.load(res).keys()
        dic2 = []
        for x in range(number):
            dic2.append(list(dic)[x])
    print(dic2)