import json
import datetime
from amadeus import Client, ResponseError


amadeus = Client(
    client_id='wT3u7CqcHTTLTgE39MajqwbOTwagAKVP',
    client_secret='BvzgQ8YlLU1zmDp3',
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
        
        with open("./algoritmoPython/cristian/vuelo.json", "w") as outfile:
            json.dump(response.data, outfile, indent=4, sort_keys=True)

    except ResponseError as error:
        raise error

ObtenerVuelos("VLC","LGW",datetime.datetime(2023,1,15),datetime.datetime(2023,1,23))