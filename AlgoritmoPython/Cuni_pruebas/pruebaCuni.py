from textwrap import indent
import requests
import json
import os, json

path_to_json = 'AlgoritmoPython/airportDataJson/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
frecuencia = dict()

for pos_json in json_files:
    with open(os.path.join(path_to_json, pos_json)) as json_file:
      json_text = json.load(json_file)
      if len(json_text['response']) > 2 :
         origen = json_text['response'][0]['dep_iata']
         frecuencia[origen] = []
         for x in json_text['response']:
            frecuencia[origen].append({
            'Destino': x['arr_iata'],
            'Hora' : x['dep_time_utc'],
            'Frecuencia': x['days']
            })

with open("AlgoritmoPython\Cuni_pruebas\prueba.json", "w") as f:
   json.dump(frecuencia, f, indent=4)    
        
