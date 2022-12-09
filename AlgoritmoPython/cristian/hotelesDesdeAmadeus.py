import json
import datetime
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='wT3u7CqcHTTLTgE39MajqwbOTwagAKVP',
    client_secret='BvzgQ8YlLU1zmDp3'
)

def ObtenerHoteles(destino: str):
    try:
        response =  amadeus.reference_data.locations.hotels.by_city.get(cityCode=destino, ratings=[3])
        
        with open("./algoritmoPython/cristian/hotel.json", "w") as outfile:
            json.dump(response.data, outfile, indent=4, sort_keys=True)

    except ResponseError as error:
        raise error

def ObtenerHabitaciones(fechaIda: datetime, fechaVuelta: datetime):
    with open('./algoritmoPython/cristian/hotel.json') as hoteles:
        listahoteles = json.load(hoteles)
    
    listahab = []

    i = 0
    for hotel in listahoteles:
        try:
            hotel_offers = amadeus.shopping.hotel_offers_search.get(
                hotelIds=hotel["hotelId"], adults=1, checkInDate=str(fechaIda.date()), checkOutDate=str(fechaVuelta.date()))
            
            if(hotel_offers.data != []): 
                listahab.append(hotel_offers.data)
                i+=1
            if(i>1): break
        except Exception: 0
        
    with open("./algoritmoPython/cristian/habitaciones.json", "w") as outfile:
        json.dump(listahab, outfile, indent=4, sort_keys=True)


def ObtenerPuntuacion():
    try:
        response = amadeus.e_reputation.hotel_sentiments.get(hotelIds = 'ALLON591')
        print(response.data)
    except ResponseError as error:
        raise error

def ObtenerHabitacionesDeCiudad(destino: str, fechaIda: datetime, fechaVuelta: datetime):
    ObtenerHoteles(destino)
    ObtenerHabitaciones(fechaIda, fechaVuelta)

    with open('./algoritmoPython/cristian/habitaciones.json') as habitaciones:
        return json.load(habitaciones)

#ObtenerHoteles("LON",datetime.datetime(2023,1,15),datetime.datetime(2023,1,23))
#ObtenerPuntuacion()
#ObtenerHabitaciones(datetime.datetime(2023,1,15),datetime.datetime(2023,1,23))
