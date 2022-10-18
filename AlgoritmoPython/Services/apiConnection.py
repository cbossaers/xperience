from amadeus import Client, ResponseError

amadeus = Client(
    client_id='H60c8yIe6mIkrrgNCc48AvkxmRTjpjRR',
    client_secret='gfqji5m9gPlPtIqi'
)


def getHotelByCity(cityCode):
    try:
        response = amadeus.get(
            '/v1/reference-data/locations/hotels/by-city', cityCode=cityCode)
        return response.data
    except ResponseError as error:
        return error


def getFlight(originLocationCode, destinationLocationCode, departureDate, adults):
    try:
        response = amadeus.get(
            '/v2/shopping/flight-offers', originLocationCode=originLocationCode, destinationLocationCode=destinationLocationCode, departureDate=departureDate, adults=adults)
        return response.data
    except ResponseError as error:
        return error


print(getFlight('SYD', 'BKK', '2022-11-01', 1))
