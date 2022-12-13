import Service
from amadeus import Client, ResponseError
import json
from datetime import date

amadeus = Client(
    client_id='H60c8yIe6mIkrrgNCc48AvkxmRTjpjRR',
    client_secret='gfqji5m9gPlPtIqi'
)

def getHabitaciones(cityCode, adults):
    hoteles = getHotelByCity(cityCode)
    count = 0
    limit = 0
    posicion = 0
    list = dict()
    
    for element in hoteles:
        if (count != len(hoteles)):
            if (limit == 108):
                # ofertas = getOfertas(hoteles[posicion-limit:posicion], adults)
                h = hoteles[109:120]
                ofertas = getOfertas(h, adults)
                print(ofertas)
                
                if(ofertas == 400):
                    list = Service.unir_diccionarios(list,ofertas)
                limit = 0
        else:
            if list:
                list = Service.unir_diccionarios(list, getOfertas(hoteles[0:posicion], adults))
            else:
                list = Service.unir_diccionarios(list, getOfertas(hoteles[posicion-limit:posicion], adults))
        count += 1
        limit += 1
        posicion += 1
    
    # i = 0
    # result = dict()
    # for element in list:
    #     if(i<len(list)):
    #         result = Service.unir_diccionarios(result, list[i])
    #     i += 1

    # return json.dumps(result, indent=2)
    return list

def getHotelByCity(cityCode):
    try:
        response = amadeus.get(
            '/v1/reference-data/locations/hotels/by-city', cityCode=cityCode)
        lista = []
        for element in response.result["data"]:
            lista.append(element["hotelId"])
        return lista
    except ResponseError as error:
        return error

def getHotelRating(hotelIds):
    try:
        response = amadeus.get(
            '/v1/e-reputation/hotel-sentiments', hotelIds=hotelIds)
        lista = []
        for element in response.result["data"]:
            if element["overallRating"] >= 30:
                lista.append(element)
        return lista
    except ResponseError as error:
        return error

def getCheapestDatesFlights(num, origin, destination, departureDate = "", oneWay = False, duration = 3, nonStop = False, maxPrice = 99999, viewBy = "DURATION"):
    try:
        if(departureDate == ""):
            today = date.today()
            nextYear = date.today()
            nextYear = nextYear.replace(year = nextYear.year + 1)
            departureDate = today.strftime("%Y-%m-%d") + "," + nextYear.strftime("%Y-%m-%d")
        response = amadeus.get(
            '/v1/shopping/flight-dates', origin=origin, destination=destination, departureDate=departureDate, oneWay=oneWay, duration=duration,nonStop=nonStop, maxPrice=maxPrice, viewBy= viewBy)
        lista = response["data"][:num]
        return lista
    except ResponseError as error:
        return error

def getOfertas(idsHoteles, adults):
    try:
        response = amadeus.get(
            '/v3/shopping/hotel-offers', hotelIds=idsHoteles, adults=adults)
        return response.result
    except ResponseError as error:
        return error


def getFlight(originLocationCode, destinationLocationCode, departureDate, adults):
    try:
        response = amadeus.get(
            '/v2/shopping/flight-offers', originLocationCode=originLocationCode, destinationLocationCode=destinationLocationCode, departureDate=departureDate, adults=adults)
        return response.result
    except ResponseError as error:
        return error



# with open('vuelosIda.json', 'w') as file:
#     json.dump(getFlight('MAD', 'AMS', '2023-02-01', 2), file, indent=4)

# with open('vuelosVuelta.json', 'w') as file:
#     json.dump(getFlight('AMS', 'MAD', '2023-02-12', 2), file, indent=4)

# with open('habitaciones.json', 'w') as file:
#     json.dump(getHabitaciones('AMS', 2), file, indent=4)
