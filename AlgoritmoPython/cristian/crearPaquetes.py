import json
import datetime
import hotelesDesdeAmadeus as h
import vuelosDesdeAmadeus as v
from pprint import pprint
from multiprocessing import Pool
from itertools import repeat

def CrearPaquete(origen: str, destino: str, fechaIda: datetime, fechaVuelta: datetime):
    habitacion = h.ObtenerHabitacionesDeCiudad(destino, fechaIda, fechaVuelta)
    vuelo = v.ObtenerVuelos(origen, destino, fechaIda, fechaVuelta)

    result = {
        "destino": destino,
        "precioTotal": (float(habitacion["offers"][0]["price"]["total"]) + float(vuelo["price"]["total"]))/2,
        "precioHotel": float(habitacion["offers"][0]["price"]["total"])/2,
        "precioIda": float(vuelo["price"]["total"])*0.58,
        "precioVuelta": float(vuelo["price"]["total"])*0.42,
        "salidaIda": vuelo["itineraries"][0]["segments"][0]["departure"]["at"],
        "llegadaIda": vuelo["itineraries"][0]["segments"][0]["arrival"]["at"],
        "duracionIda": vuelo["itineraries"][0]["duration"],
        "salidaVuelta": vuelo["itineraries"][1]["segments"][0]["departure"]["at"],
        "llegadaVuelta": vuelo["itineraries"][1]["segments"][0]["arrival"]["at"],
        "duracionVuelta": vuelo["itineraries"][1]["duration"],
        "hotelNombre": habitacion["hotel"]["name"],
        "habitacion": habitacion["offers"][0]["room"]["typeEstimated"]["bedType"] + " " + habitacion["offers"][0]["room"]["typeEstimated"]["category"]
    }
    
    pprint(result)
    return result

#CrearPaquete("VLC","PAR",datetime.datetime(2023,1,15),datetime.datetime(2023,1,23))

if __name__ == '__main__':
    args1 = list(repeat("VLC",10))
    args2 = ["PAR", "LON", "AMS", "FCO", "BER", "BRU", "CDG", "MUC", "ARN", "PMI"]
    args3 = list(repeat(datetime.datetime(2023,1,15), 10))
    args4 = list(repeat(datetime.datetime(2023,1,23),10))

    res = []
    with Pool(processes=10) as pool:
        res = pool.starmap(CrearPaquete, zip(args1,args2,args3,args4))

    res_list1 = [r[0] for r in res]

    print("------------------------")
    print(res_list1)