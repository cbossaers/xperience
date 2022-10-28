from operator import index
import string
from textwrap import indent
import json
import os, json
import datetime


path_to_json = 'AlgoritmoPython/seleccionAeropuertos/airportDestinations'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
frecuencia = dict()
sitio = dict()
dias_=['mon','tue','wed','thu','fri','sat','sun']
diasNormalizados=['L','M','X','J','V','S','D']

def DayToNumber(lista : list) :
   for idx, x in enumerate(lista) :
      lista[idx] = dias_.index(x)
   return sorted(lista)

def DayNormalizado(lista : list) :
   for idx, x in enumerate(lista) :
      lista[idx] = diasNormalizados[x]
   return lista


def CargarViajes() :
   for pos_json in json_files:
    with open(os.path.join(path_to_json, pos_json)) as json_file:
      json_text = json.load(json_file)
      if len(json_text['response']) > 2 :
         origen = json_text['response'][0]['dep_iata']
         frecuencia[origen] = dict()
         for x in json_text['response']:
            destino = x['arr_iata']
            dia = DayToNumber(x['days'])
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
               sitio[destino]['dias'] = sorted(res)
         frecuencia[origen] = sitio      
   with open("AlgoritmoPython\Cuni_pruebas\prueba_frec.json", "w") as f:
      json.dump(frecuencia, f, indent=4, sort_keys=True) 


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

def Destinos(n : int) :
   with open('AlgoritmoPython\Cuni_pruebas\prueba_frec.json') as json_file:
      json_text = json.load(json_file)
   with open('AlgoritmoPython\Cuni_pruebas\prueba_frec.json') as desti:
      destinosList = json.load(desti)   
   destinos = []
   for origen in json_text.keys():
      cont = 1
      destinosOrigen = json_text[origen].keys()
      for destino in destinosList.keys():
         if destino in destinosOrigen and origen != destino:
            dias = json_text[origen][destino]['dias']
            dias = DayNormalizado(dias)
            destinos.append(
               {"Origen" : origen, "Destino" : destino, "Dias" : dias}
            )
            if cont == n :
               break
            cont+= 1
   with open("AlgoritmoPython\Cuni_pruebas\destinos.json", "w") as f:
      json.dump(destinos, f, indent=2)       

def Media(x:list) :
   return sum(x) / len(x)




 