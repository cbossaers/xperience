import json
import random
from datetime import datetime
from amadeus import Client, ResponseError
from pprint import pprint

amadeus = Client(
    client_id='evAyCfGSi015tprOjzDUWdBUQdeK54PB',
    client_secret='rDYX0wAOqCj6roes'
)

def Fake(origen, fechaIda, fechaVuelta, presupuesto):
    args = ["PAR", "LON", "AMS", "ROM", "BER", "BRU", "MUC", "FRA", "OPO", "ZRH", "DUB", "LIS"]
    args2 = ["Hotel Grand Traveler Stand ", "Prime Statue Hotel ", "NH Hotel ", "Main Park Hotel ", "Travelodge ", "Meliá Hotels International ", "Radisson Hotel Group ", "Scandic Hotels ", "IHG ", "Hilton ", "Novotel ", "Premier Hotel ", "ibis ", "Accor Central ", "Mariott ", "FRHI "]

    res = []

    with open('C:/Users/Cristian/Documents/bluesky/algoritmoPython/cristian/nombresAeropuertos.json', 'r') as f:
        data = json.load(f)

    for arg in args:

        m = int(fechaIda[5:7]) + int(fechaIda[8:10])
        n = int(fechaVuelta[5:7]) + int(fechaVuelta[8:10])

        print(m)
        print(n)

        a = random.randint(150,presupuesto)
        b = int(a*0.6)
        c = int(a*0.175)
        d = int(a*0.225)
        e = random.randint(0,15)

        x = random.randint(1,2)
        y = random.randint(x+1,2+x)

        horaida1 = 10 + x
        horaida2 = 11 + y
        horavuelta1 = 15 + x
        horavuelta2 = 16 + y
        duracionida = horaida2 - horaida1 - 1
        duracionvuelta = horavuelta2 - horavuelta1 - 1

        result = {
                    "origen": TransformarOrigen(origen),
                    "destino": data[arg]["nombre"],
                    "precioTotal": a,
                    "precioHotel": b,
                    "precioIda": c,
                    "precioVuelta": d,
                    "salidaIda": fechaIda+"T"+str(horaida1)+":50:00",
                    "llegadaIda": fechaIda+"T"+str(horaida2)+":10:00",
                    "duracionIda": "PT"+str(duracionida)+"H20M",
                    "salidaVuelta": fechaVuelta+"T"+str(horavuelta1)+":45:00",
                    "llegadaVuelta": fechaVuelta+"T"+str(horavuelta2)+":20:00",
                    "duracionVuelta": "PT"+str(duracionvuelta)+"H25M",
                    "hotelNombre": args2[e]+data[arg]["nombre"],
                    "foto": data[arg]["foto"]
                }
        res.append(result)

    return res

def TransformarOrigen(origen):
    if(origen == "MAD"): origen = "Madrid"
    elif(origen == "VLC"): origen = "Valencia"
    elif(origen == "ALC"): origen = "Alicante"
    elif(origen == "AGP"): origen = "Málaga"
    elif(origen == "BCN"): origen = "Barcelona"
    else: origen = "Sevilla"

    return origen

#Fake("MAD","2023-05-17","2023-05-25",1000)

string = "2023-05-17"
print(int(string[5:7]))
print(int(string[8:10]))