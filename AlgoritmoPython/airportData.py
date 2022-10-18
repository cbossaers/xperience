import requests
import json

airports = ['MAD', 'BCN', 'PMI', 'AGP', 'ALC', 'LPA', 'TFS', 'LPC', 'IBZ', 'SVQ']


for airport in airports:
    params = {
    'api_key': 'b2aa36ba-24ae-4496-a278-e7593719af77',
    'dep_iata': airport
    }
    method = 'routes'
    api_base = 'http://airlabs.co/api/v9/'
    api_result = requests.get(api_base+method, params)
    api_response = api_result.json()

    filename = airport + '.json'

    with open(filename, "w") as outfile:
        json.dump(api_response, outfile, indent=4, sort_keys=True)