import datetime
from amadeus import Client, ResponseError
from multiprocessing import Pool
from itertools import repeat

amadeus = Client(
    client_id='0sxAuGfYEo2XMONAV020GNRpoi5ACgYb',
    client_secret='dpBQ1LE6xJtVvPyB'
)

def ObtenerHoteles(destino: str):
    try:
        response =  amadeus.reference_data.locations.hotels.by_city.get(cityCode=destino, ratings=[3])

        res = []

        for elem in response.data:
            res.append(elem["hotelId"])

        res = [res[i:i+10] for i in range(0,len(res),10)]
        return res

    except ResponseError as error:
        raise error

def ObtenerHabitaciones(hoteles, fechaIda: datetime, fechaVuelta: datetime):
    listahab = []

    try:
        hotel_offers = amadeus.shopping.hotel_offers_search.get(
            hotelIds=hoteles, adults=1, checkInDate=str(fechaIda.date()), checkOutDate=str(fechaVuelta.date()))
        
        if(hotel_offers.data != []): 
            listahab.append(hotel_offers.data)

    except Exception: 0

    if listahab == []: listahab.append("")

    return listahab

def ObtenerHabitacionesDeCiudad(destino: str, fechaIda: datetime, fechaVuelta: datetime):
    if __name__ == '__main__':
        hoteles = ObtenerHoteles(destino)

        res = []

        with Pool() as pool:
            res = pool.starmap(ObtenerHabitaciones, zip(hoteles, list(repeat(fechaIda, 10)), list(repeat(fechaVuelta, 10))))

        habitaciones = [r[0] for r in res]

        return habitaciones

ObtenerHabitacionesDeCiudad("PAR", datetime.datetime(2023,5,10), datetime.datetime(2023,5,16))