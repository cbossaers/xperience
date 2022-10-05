import requests
import json

airports = ['MAD', 'BCN', 'PMI', 'AGP', 'ALC', 'LPA', 'TFS', 'LPC', 'IBZ', 'SVQ']

params = {
  'api_key': 'b2aa36ba-24ae-4496-a278-e7593719af77',
  'dep_iata': 'MAD'
}
method = 'routes'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params)
api_response = api_result.json()

#print(json.dumps(api_response, indent=4, sort_keys=True))

with open("datos.json", "w") as outfile:
    json.dump(api_response, outfile, indent=4, sort_keys=True)