from operator import index
import string
from textwrap import indent
import json
import os, json
import datetime


path_to_json = 'AlgoritmoPython/airportDataJson/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
frecuencia = dict()
sitio = dict()
dias_=['mon','tue','wed','thu','fri','sat','sun']

def dayToNumber(lista : list) :
   for idx, x in enumerate(lista) :
      lista[idx] = dias_.index(x)
   return sorted(lista)

for pos_json in json_files:
    with open(os.path.join(path_to_json, pos_json)) as json_file:
      json_text = json.load(json_file)
      if len(json_text['response']) > 2 :
         origen = json_text['response'][0]['dep_iata']
         frecuencia[origen] = []
         for x in json_text['response']:
            dia = dayToNumber(x['days'])
            if sitio.get(x['arr_iata']) == None :
               sitio[x['arr_iata']] = dia
            else : 
               res = sitio[x['arr_iata']]
               for i in dia: 
                  if i not in res: 
                     res.append(i) 
               sitio[x['arr_iata']] = sorted(res)     
         frecuencia[origen].append(sitio)      

with open("AlgoritmoPython\Cuni_pruebas\prueba_frec.json", "w") as f:
   json.dump(frecuencia, f, indent=4, sort_keys=True) 

def getDias(origen,destino):
   with open('AlgoritmoPython\Cuni_pruebas\prueba_frec.json') as json_file:
      json_text = json.load(json_file)
   return json_text[origen][0][destino]

with open('AlgoritmoPython\Cuni_pruebas\prueba_frec.json') as json_file:
      json_text = json.load(json_file)


def paquetes(origen, fecha_ida : datetime, fecha_vuelta : datetime, presupuesto : int) :
   with open('AlgoritmoPython\Cuni_pruebas\prueba_frec.json') as json_file:
      json_text = json.load(json_file)
   ida = fecha_ida.weekday() 
   vuelta = fecha_vuelta.weekday()
   destinos = []
   for idx, x in enumerate(json_text[origen][0]) :
      print(x)
      if ida in json_text[origen][0].get(x) : 
         destinos.append(x) 
         

ida = datetime.datetime.today()
vuelta = datetime.datetime.today()
presupuesto = 66
origen = 'AGP'
paquetes(origen,ida,vuelta,presupuesto)
   

   
   
        
