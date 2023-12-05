import datetime
from amadeus import Client, ResponseError
from pprint import pprint

amadeus = Client(
    client_id='evAyCfGSi015tprOjzDUWdBUQdeK54PB',
    client_secret='rDYX0wAOqCj6roes'
)

def ObtenerVuelos(origen: str, destino: str, fechaIda: datetime, fechaVuelta: datetime):
    data = {
        "currencyCode": "EUR",
        "originDestinations": [{
            "id": "1",
            "originLocationCode": origen,
            "destinationLocationCode": destino,
            "departureDateTimeRange": {
                "date": str(fechaIda.date()),
                "time": "00:00:00"
            }
        },
        {
            "id": "2",
            "originLocationCode": destino,
            "destinationLocationCode": origen,
            "departureDateTimeRange": {
                "date": str(fechaVuelta.date()),
                "time": "00:00:00"
            }
        }],
        "travelers": [{
            "id": "1",
            "travelerType": "ADULT"
        }],
        "sources": [
            "GDS"
        ],
        "searchCriteria": {
            "maxFlightOffers": 1,
            "flightFilters": {
                "maxFlightTime": 120
            }
        }
    }

    try:
        response = amadeus.shopping.flight_offers_search.post(data)
        
        return response.data

    except ResponseError as error:
        raise error

#pprint(ObtenerVuelos("VLC","LON",datetime.datetime(2023,7,10),datetime.datetime(2023,7,18)))