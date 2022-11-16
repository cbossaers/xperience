import Service
import ApiConnection
import os
import json
from datetime import date


def getHabitacion(origen, presupuesto, fechaida, fechavuelta, adultos):
    listPlaces = getListOrginAndDestination()
    destinos = []
    habitaciones = dict()
    limit = 0

    if origen in listPlaces.keys():
        destinos = list(listPlaces.get(origen))

    if destinos:
        for destino in destinos:
            vuelosIdaDestino = ApiConnection.getFlight(
                origen, destino, fechaida, adultos)
            vuelosVueltaDestino = ApiConnection.getFlight(
                destino, origen, fechavuelta, adultos)
            if vuelosIdaDestino and vuelosVueltaDestino:
                newHab = ApiConnection.getHabitaciones(destino, adultos)
                if newHab:
                    if limit < 2:
                        vuelosIda = getVuelosFechas(vuelosIdaDestino, fechaida)
                        vuelosVuelta = getVuelosFechas(vuelosVueltaDestino, fechavuelta)
                        if vuelosIda and vuelosVuelta:
                            habitaciones = addHabitaciones(habitaciones,
                                                    newHab, fechaida, fechavuelta, presupuesto, vuelosIda, vuelosVuelta)
                            limit += 1
    return habitaciones


def getVuelosFechas(vuelosDestino, fechaida):
    vuelos = dict()
    for vuelo in vuelosDestino["data"]:
        for itineraries in vuelo["itineraries"]:
            for segments in itineraries["segments"]:
                if fechaida in segments["departure"]["at"]:
                    vuelos = Service.unir_diccionarios(vuelos, vuelo)
    return vuelos


def addHabitaciones(habitaciones, newHab, fechaida, fechavuelta, presupuesto, vuelosIda, vuelosVuelta):
    for habitacion in newHab["data"]:
        for offer in habitacion["offers"]:
            if offer["checkInDate"] == fechaida:
                idaSplit = fechaida.split('-')
                ida = date(int(idaSplit[0]), int(
                    idaSplit[1]), int(idaSplit[2]))
                vueltaSplit = fechavuelta.split('-')
                vuelta = date(int(vueltaSplit[0]), int(
                    vueltaSplit[1]), int(vueltaSplit[2]))
                duracion = (vuelta - ida).days
                paquetes = precioPaquete(offer["price"]["total"], duracion, vuelosIda, vuelosVuelta, presupuesto, newHab)
                return paquetes
    return habitaciones

def precioPaquete(nocheHabitacion, duracion, vuelosIda, vuelosVuelta, presupuesto, newHab):
    paquetes = dict()
    # for vueloIda in vuelosIda:
    for vueloIda in vuelosIda["data"]:
        # for vueloVuelta in vuelosVuelta:
        for vueloVuelta in vuelosVuelta["data"]:
            print(vueloIda["price"]["total"])
            print(vueloVuelta["price"]["total"])
            precio = float(nocheHabitacion) * (duracion - 1) + vueloIda["price"]["total"] + vueloVuelta["price"]["total"]
            if precio <= presupuesto:
                # CREAR HABITACION
                # CREAR VUELO IDA
                # CREAR VUELO VUELTA
                # CREAR PAQUETE
                # Buscar por código de 
                paquetes = Service.unir_diccionarios(paquetes, vueloIda)
                paquetes = Service.unir_diccionarios(paquetes, vueloVuelta)
                paquetes = Service.unir_diccionarios(paquetes, newHab)
    return paquetes

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


print(getHabitacion('MAD', 600, '2022-11-16', '2022-11-22', 2))
