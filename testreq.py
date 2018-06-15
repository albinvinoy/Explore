import requests
import json

api_key = "_9lSdEylcyUrURMdo0RU4tmV3wmvco0MXaWBk3mcxomqoZShLXPcl1YZOfg-4qHKDVXFZeIPPRIbPZdv8LeHoKPVDGNV90wULEey0tMdHVphlHhpV_sBAsoFHfknW3Yx"
api_host = "https://api.yelp.com/v3/businesses/search"


term = 'dinner'
location = 'San Francisco, CA'
SEARCH_LIMIT = 3

headers = {
    'Authorization': 'Bearer %s' % api_key,
}

url_params = {
    'term': term.replace(' ', '+'),
    'latitude': latitude,
    'longitude' : longitude,
    'limit': SEARCH_LIMIT
}


response = requests.get(api_host, headers=headers, params=url_params)
print(response.json())