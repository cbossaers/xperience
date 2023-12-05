import datetime
from amadeus import Client, ResponseError
from concurrent.futures import ProcessPoolExecutor as Pool
from itertools import repeat
from pprint import pprint
import json

amadeus = Client(
    client_id='evAyCfGSi015tprOjzDUWdBUQdeK54PB',
    client_secret='rDYX0wAOqCj6roes'
)

def ObtenerHoteles(destino: str):
    try:
        response =  amadeus.reference_data.locations.hotels.by_city.get(cityCode=destino, ratings=[3])

        res = []

        for elem in response.data:
            res.append(elem["hotelId"])

        res = [res[i:i+30] for i in range(0,len(res),30)]
        return res

    except ResponseError as error:
        raise error

def ObtenerHabitaciones(hoteles, fechaIda: datetime, fechaVuelta: datetime):
    listahab = []

    try:
        hotel_offers = amadeus.shopping.hotel_offers_search.get(
            hotelIds=hoteles, adults=1, checkInDate=fechaIda, checkOutDate=fechaVuelta)
        
        if(hotel_offers.data != []): 
            listahab.append(hotel_offers.data)

    except Exception as error: print(error)

    if listahab == []: listahab.append("")

    return listahab

def ObtenerHabitacionesDeCiudad(destino: str, fechaIda: datetime, fechaVuelta: datetime):
    if __name__ == '__main__':
        hoteles = ObtenerHoteles(destino)

        res = []

        with Pool() as pool:
            for x in pool.map(ObtenerHabitaciones, hoteles, list(repeat(fechaIda, 10)), list(repeat(fechaVuelta, 10))):
                res.append(x)

        #for hotel in hoteles:
        #   res.append(ObtenerHabitaciones(hotel,fechaIda,fechaVuelta))

        habitaciones = list(filter(None, res[0]))

        return habitaciones

#pprint(ObtenerHabitacionesDeCiudad("PAR",datetime.datetime(2023,7,10),datetime.datetime(2023,7,18)))