import json
import os
def getJson():
    # assign directory
    directory = 'AlgoritmoPython/airportDataJson'
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
    print("Added" + stradded)
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))
    with open ("AlgoritmoPython/cantidad_de_viajes_a_destino.json", "w") as res:
        json.dump(result,res, indent = 2)
    
def getNumberOfTravels(number: int):
    with open ("AlgoritmoPython/cantidad_de_viajes_a_destino.json", "r") as res:
        dic = json.load(res)
    return list(dic.keys())[0:number]

print(getNumberOfTravels(10))''