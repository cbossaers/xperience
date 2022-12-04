from urllib.request import urlopen
from flask import jsonify
from flask_restful import Resource, Api, reqparse, request
import pandas as pd
import json
from amadeus import Client, ResponseError, Location
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

amadeus = Client(
    client_id='wT3u7CqcHTTLTgE39MajqwbOTwagAKVP',
    client_secret='BvzgQ8YlLU1zmDp3',
)

def ObtenerVuelos(origen: str):
    a = {
        "currencyCode": "USD",
        "originDestinations": [{
            "id": "1",
            "originLocationCode": "MAD",
            "destinationLocationCode": "NRT",
            "departureDateTimeRange": {
                "date": "2022-03-25",
                "time": "00:00:00"
            }
        },
        {
            "id": "2",
            "originLocationCode": "NRT",
            "destinationLocationCode": "MAD",
            "departureDateTimeRange": {
                "date": "2023-04-14",
                "time": "00:00:00"
            }
        }],
        "travelers": [{
            "id": "1",
            "travelerType": "ADULT"
        },
        {
            "id": "2",
            "travelerType": "CHILD"
        }],
        "sources": [
            "GDS"
        ]
    }

    try:
        response = amadeus.shopping.flight_offers_search.post(a)
        
        with open("aa.json", "w") as outfile:
            json.dump(response.data, outfile, indent=4, sort_keys=True)

    except ResponseError as error:
        print(error)
        raise error

test()