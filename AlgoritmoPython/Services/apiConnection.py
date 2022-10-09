import requests

BASE_URL = 'test.api.amadeus.com/v3'

res = requests.get(BASE_URL + '/reference-data/locations/hotels/by-city/CUN')

print(res)