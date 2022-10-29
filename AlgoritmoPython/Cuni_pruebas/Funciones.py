from operator import index
import string
from textwrap import indent
import json
import os, json
import datetime


path_to_json = 'AlgoritmoPython/seleccionAeropuertos/airportDestinations'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
dias_=['mon','tue','wed','thu','fri','sat','sun']
diasNormalizados=['L','M','X','J','V','S','D']
airp = ['MAD', 'BCN', 'AGP', 'ALC', 'SVQ', 'VLC']

def SortSemana(lista : list) :
   d = [] 
   for idx, x in enumerate(lista) :
      if x in lista :
         d.append(diasNormalizados[idx])
   return d      

def Media(x:list) :
   return sum(x) / len(x)

def DestinosList(n : int) :
    with open('AlgoritmoPython/seleccionAeropuertos/frecuenciaDestinos.json') as desti:
        destinosList = json.load(desti)
    destinos = list(destinosList.keys())  
    return destinos[:n]

def Paquetes(origen, fecha_ida : datetime, fecha_vuelta : datetime, presupuesto : int) :
   with open('AlgoritmoPython\Cuni_pruebas\prueba_frec.json') as json_file:
      json_text = json.load(json_file)
   ida = fecha_ida.weekday() 
   vuelta = fecha_vuelta.weekday()
   destinos = []
   for x in json_text[origen].keys():
      aeropuertos = json_text[origen][x]['dias']
      if ida in aeropuertos and vuelta in aeropuertos : 
         destinos.append(x) 
   with open("AlgoritmoPython\Cuni_pruebas\prueba.json", "w") as f:
      json.dump(destinos, f, indent=4, sort_keys=True)

def ProcesarJson(json_text, destinosArray,t) :
    sitio = dict()        
    for x in json_text['response']:
        destino = x['arr_iata']
        if destino in destinosArray :
            dia = x['days']
            precio = 666
            if sitio.get(destino) == None :
                sitio[destino] = dict()
                sitio[destino] = {
                'dias' : dia,
                'precio' : precio
                }
            else : 
                res = sitio[destino]['dias']
                res = list(set(res) | set(dia))  
                sitio[destino]['dias'] = res
    for x in sitio.keys() :
        sitio[x]['dias'] =  SortSemana(sitio[x]['dias'])
    return sitio            

def VuelosFiltados(origenes : list, destinos : list , origenPath, printPath) :
    frecuencia = dict()
    for airport in origenes:
        filename = "./AlgoritmoPython/seleccionAeropuertos/"+ origenPath +"/" + airport + '.json'
        with open(filename) as desti:
            apiResponse = json.load(desti)
        if len(apiResponse['response']) > 2 :
            origen = apiResponse['response'][0]['dep_iata']
            frecuencia[origen] = dict()
            frecuencia[origen] = ProcesarJson(apiResponse, destinos)
    with open("AlgoritmoPython/Cuni_pruebas/"+ printPath +'.json', "w") as f:
        json.dump(frecuencia, f, indent=2)    




 