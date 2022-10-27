import apiConnection
import os, json

def getHabitacion(origen, presupuesto, fechaida, fechavuelta):
    pathJson = 'AlgoritmoPython/seleccionAeropuertos/airportDestinations/'
    content = os.listdir(pathJson)
    airportDestinations = []
    
    for file in content:
        if os.path.isfile(os.path.join(pathJson, file)) and file.endswith('.json'):
            airportDestinations.append(file)
            
    # for airport in airportDestinations:
    #    return airport
    # apiConnection.getFlight()
    return airportDestinations[0]