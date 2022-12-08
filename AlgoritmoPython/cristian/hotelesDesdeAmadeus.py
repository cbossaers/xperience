import json
import datetime
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='wT3u7CqcHTTLTgE39MajqwbOTwagAKVP',
    client_secret='BvzgQ8YlLU1zmDp3'
)

def ObtenerHoteles(destino: str, fechaIda: datetime, fechaVuelta: datetime):
    try:
        response =  amadeus.reference_data.locations.hotels.by_city.get(cityCode=destino)
        
        with open("./algoritmoPython/cristian/hotel.json", "w") as outfile:
            json.dump(response.data, outfile, indent=4, sort_keys=True)

    except ResponseError as error:
        raise error

def ObtenerHabitaciones(fechaIda: datetime, fechaVuelta: datetime):
    with open('./algoritmoPython/cristian/hotel.json') as hoteles:
        listahoteles = json.load(hoteles)
    
    listahab = {}

    for hotel in listahoteles:
        hotel_offers = amadeus.shopping.hotel_offers.get(
            hotelIds=hotel["hotelId"], adults=1, checkInDate=str(fechaIda.date()), checkOutDate=str(fechaVuelta.date()))
        
        listahab.update(hotel_offers.data)
        
        with open("./algoritmoPython/cristian/habitaciones.json", "a") as outfile:
            json.dump(listahab, outfile, indent=4, sort_keys=True)


#ObtenerHoteles("PAR",datetime.datetime(2023,1,15),datetime.datetime(2023,1,23))
#ObtenerPuntuacion()
#ObtenerHabitaciones(datetime.datetime(2023,1,15),datetime.datetime(2023,1,23))