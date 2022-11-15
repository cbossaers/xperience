import Service
import ApiConnection
import os
import json


def getHabitacion(origen, presupuesto, fechaida, fechavuelta, adultos):
    listPlaces = getListOrginAndDestination()
    destinos = []
    habitaciones = dict()

    if origen in listPlaces.keys():
        destinos = list(listPlaces.get(origen))

    if destinos:
        for destino in destinos:
            vuelosDestino = ApiConnection.getFlight(origen, destino, fechaida, adultos)
            if vuelosDestino:
                newHab = ApiConnection.getHabitaciones(destino, adultos)
                if newHab:
                    habitaciones = addHabitaciones(habitaciones,
                                                newHab, fechaida, fechavuelta, presupuesto)

    return habitaciones


def addHabitaciones(habitaciones, newHab, fechaida, fechavuelta, presupuesto):
    for habitacion in newHab["data"]:
        for offer in habitacion["offers"]:
            if (offer["checkInDate"] == fechaida
                and offer["checkOutDate"] == fechavuelta):
                for price in offer["price"]:
                    if (price["total"] <= presupuesto):
                        return Service.unir_diccionarios(habitaciones, newHab)

    return habitaciones


def getListOrginAndDestination():
    listPlaces = dict()
    # RUTA EN EJECUCIÓN Y DEPURAR:
    # jsonDestinationPath = os.path.abspath(r'../bluesky/AlgoritmoPython/seleccionAeropuertos/airportDestinations')
    # RUTA EN EJECUCIÓN:
    jsonDestinationPath = os.path.abspath(
        r'../seleccionAeropuertos/airportDestinations')
    for posJson in os.listdir(jsonDestinationPath):
        if posJson.endswith('.json'):
            with open(os.path.join(jsonDestinationPath, posJson)) as destination:
                listPlaces = addOrginAndDestination(
                    listPlaces, json.load(destination))

    return listPlaces


def addOrginAndDestination(listPlaces, json):
    # arr_iata ORIGEN
    # dep_iata DESTINO
    for destination in json["response"]:
        origin = destination['arr_iata']
        destination = destination['dep_iata']
        values = []
        if listPlaces:
            if origin in listPlaces.keys():
                values = list(listPlaces.get(origin))
                if destination not in values:
                    values.append(destination)
                listPlaces[origin] = values
            else:
                values.append(destination)
                listPlaces[origin] = values
        else:
            values.append(destination)
            listPlaces[origin] = values

    return listPlaces


print(getHabitacion('MAD', 200, '21/11/2022', '26/11/2022', 2))
