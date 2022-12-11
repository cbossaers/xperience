import json
import datetime
import hotelesDesdeAmadeus as h
import vuelosDesdeAmadeus as v
from pprint import pprint
from itertools import repeat
#from concurrent.futures import ProcessPoolExecutor as Pool
import time
import random

def CrearPaquete(origen: str, destino: str, fechaIda: datetime, fechaVuelta: datetime):

    vuelo = v.ObtenerVuelos(origen, destino, fechaIda, fechaVuelta)
    habitacion = h.ObtenerHabitacionesDeCiudad(destino, fechaIda, fechaVuelta)
    
    with open('./algoritmoPython/cristian/nombresAeropuertos.json', 'r') as f:
        data = json.load(f)

    if(len(habitacion)==0 or len(vuelo)==0): return
    else: 
        habitacion = habitacion[0][0]
        vuelo = vuelo[0]

    x = random.uniform(0.3,0.7)

    result = {
        "destino": data[destino]["nombre"],
        "precioTotal": (float(habitacion["offers"][0]["price"]["total"]) + float(vuelo["price"]["total"]))/2,
        "precioHotel": float(habitacion["offers"][0]["price"]["total"])/2,
        "precioIda": float(vuelo["price"]["total"])*x,
        "precioVuelta": float(vuelo["price"]["total"])*(1-x),
        "salidaIda": vuelo["itineraries"][0]["segments"][0]["departure"]["at"],
        "llegadaIda": vuelo["itineraries"][0]["segments"][0]["arrival"]["at"],
        "duracionIda": vuelo["itineraries"][0]["duration"],
        "salidaVuelta": vuelo["itineraries"][1]["segments"][0]["departure"]["at"],
        "llegadaVuelta": vuelo["itineraries"][1]["segments"][0]["arrival"]["at"],
        "duracionVuelta": vuelo["itineraries"][1]["duration"],
        "hotelNombre": habitacion["hotel"]["name"],
        "foto": data[destino]["foto"]
    }
    
    return result

def GenerarPaquetes(origen: str, fechaIda: datetime, fechaVuelta: datetime):
    if __name__ == '__main__':
        args = ["PAR", "LON", "AMS", "ROM", "BER", "BRU", "MUC", "FRA", "OPO", "ZRH", "DUB", "LIS"]

        res = []

        a = time.time()
        for x in args:
            res.append(CrearPaquete(origen,x,fechaIda,fechaVuelta))

        #with Pool() as pool:
        #    pool.starmap(CrearPaquete, zip(list(repeat(origen,7)), args, list(repeat(fechaIda, 7)), list(repeat(fechaVuelta, 7))))

        #x = [r[0] for r in res]

        with open("./algoritmoPython/cristian/res.json", "w") as outfile:
            json.dump(res, outfile, indent=4, sort_keys=True)

        print(str(time.time()-a))
        return outfile

GenerarPaquetes("MAD", datetime.datetime(2023,5,10), datetime.datetime(2023,5,16))