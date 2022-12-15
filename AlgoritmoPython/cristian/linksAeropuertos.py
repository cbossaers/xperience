import json

a = {
    "ACE": {
        "nombre": "Lanzarote",
        "foto": "https://media.traveler.es/photos/6279555a5b37ba40f6561b1e/16:9/w_2580,c_limit/Jameos%20piscina%2008_LR_%C2%A9%20CACT%20Lanzarote.jpg",
    },
    "AMS": {
        "nombre": "Amsterdam",
        "foto": "https://media.traveler.es/photos/6231abc7d03e1c5549e648ca/16:9/w_2560%2Cc_limit/The%2520Best%2520Places%2520for%2520Female%2520Solo%2520Travelers_Amsterdam_GettyImages-923546342.jpg",
    },
    "ARN": {
        "nombre": "Estocolmo",
        "foto": "https://a.cdn-hotels.com/gdcs/production160/d1943/a0fe0b3e-1469-412a-a45e-276f65e77702.jpg?impolicy=fcrop&w=800&h=533&q=medium",
    },
    "BER": {
        "nombre": "Berlin",
        "foto": "https://cdn2.hometogo.net/assets/media/pics/1200_628/611a5609415e7.jpg",
    },
    "BIO": {
        "nombre": "",
        "foto": "",
    },
    "BRU": {
        "nombre": "",
        "foto": "",
    },
    "CDG": {
        "nombre": "",
        "foto": "",
    },
    "DUB": {
        "nombre": "",
        "foto": "",
    },
    "FCO": {
        "nombre": "",
        "foto": "",
    },
    "FRA": {
        "nombre": "",
        "foto": "",
    },
    "FUE": {
        "nombre": "",
        "foto": "",
    },
    "IBZ": {
        "nombre": "",
        "foto": "",
    },
    "LGW": {
        "nombre": "",
        "foto": "",
    },
    "LHR": {
        "nombre": "",
        "foto": "",
    },
    "LIS": {
        "nombre": "",
        "foto": "",
    },
    "LPA": {
        "nombre": "",
        "foto": "",
    },
    "MAH": {
        "nombre": "",
        "foto": "",
    },
    "MUC": {
        "nombre": "",
        "foto": "",
    },
    "MXP": {
        "nombre": "",
        "foto": "",
    },
    "OPO": {
        "nombre": "",
        "foto": "",
    },
    "OSL": {
        "nombre": "",
        "foto": "",
    },
    "OVD": {
        "nombre": "",
        "foto": "",
    },
    "PMI": {
        "nombre": "",
        "foto": "",
    },
    "SCQ": {
        "nombre": "",
        "foto": "",
    },
    "SDR": {
        "nombre": "",
        "foto": "",
    },
    "TFN": {
        "nombre": "",
        "foto": "",
    },
    "VGO": {
        "nombre": "",
        "foto": "",
    },
    "ZRH": {
        "nombre": "",
        "foto": "",
    },
}

with open("./algoritmoPython/cristian/habitaciones.json", "w") as outfile:
        json.dump(a, outfile, indent=4, sort_keys=True)