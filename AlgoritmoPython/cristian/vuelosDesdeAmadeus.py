import datetime
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='0sxAuGfYEo2XMONAV020GNRpoi5ACgYb',
    client_secret='dpBQ1LE6xJtVvPyB'
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
                "time": str(fechaIda.time())
            }
        },
        {
            "id": "2",
            "originLocationCode": destino,
            "destinationLocationCode": origen,
            "departureDateTimeRange": {
                "date": str(fechaVuelta.date()),
                "time": str(fechaVuelta.time())
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

#print(ObtenerVuelos("VLC","LON",datetime.datetime(2023,3,1),datetime.datetime(2023,3,8)))