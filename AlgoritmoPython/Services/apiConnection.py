import Service
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='H60c8yIe6mIkrrgNCc48AvkxmRTjpjRR',
    client_secret='gfqji5m9gPlPtIqi'
)

def getHabitaciones(cityCode, adults):
    hoteles = getHotelByCity(cityCode)
    count = 0
    limit = 0
    posicion = 0
    list = []
    
    for element in hoteles:
        if (count != len(hoteles)):
            if (limit == 108):
                list.append(getOfertas(
                    hoteles[posicion-limit:posicion], adults))
                limit = 0
        else:
            if (list == []):
                list.append(getOfertas(hoteles[0:posicion], adults))
            else:
                list.append(getOfertas(hoteles[posicion-limit:posicion], adults))
        count += 1
        limit += 1
        posicion += 1
    
    i = 0
    result = {}
    for element in list:
        if(i<len(list)):
            result = Service.unir_diccionarios(result, list[i])
        i += 1
    # return json.dumps(result, indent=2)
    return result

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