from django.shortcuts import render, HttpResponse
import requests
from .accessKey import GEO_ACCESS_KEY, YELP_API_KEY
# Create your views here.

#main - make request
def makeRequest(url, params=None, headers=None):
    response = requests.get(url, headers=headers, params=params)
    return response



# access the ipstack to get geo location
def getGeoCoordinates():
    baseUrl = "http://api.ipstack.com/check?"

    url_params = {
        "access_key" : GEO_ACCESS_KEY,
        "security" : 1,
        "fields" : "main"
    }
    # baseUrl = "http://api.ipstack.com/check?access_key={}&security=1&fields=main".format(GEO_ACCESS_KEY)
    response = makeRequest(baseUrl, params=url_params)
    if response.status_code == 200:
        data = response.json()
        return [data["latitude"], data["longitude"]]
    else:
        # print("Failed to get response")
        return [34.0522, 118.2437] #default to LA



#yelp api

def getYelpInfo(keyword="", coordinates=[]):
    term = keyword or "dinner" # get from form
    SEARCH_LIMIT = 1 # 10 as default
    url = "https://api.yelp.com/v3/businesses/search"

    headers = {
        'Authorization': 'Bearer %s' % YELP_API_KEY,
    }

    url_params = {
        'term': term.replace(' ', '+'),
        'latitude': coordinates[0],
        'longitude' : coordinates[1],
        'limit': SEARCH_LIMIT
    }

    response = makeRequest(url=url, params=url_params, headers=headers)
    return response




#main view functions
def index(request):
    return render(request, 'exploree/index.html')


def food(request):
    r = getYelpInfo('dinner', getGeoCoordinates())
    if r.status_code==200:
        return render(request, 'exploree/food.html', context={'raw_data':r.json()})
    else:
        return HttpResponse("Failed to Load Data {}".format(r))

def activitites(request):
    r = getYelpInfo('activities', getGeoCoordinates())
    if r.status_code==200:
        return render(request, 'exploree/activities.html', context={'raw_data':r.json()})
    else:
        return HttpResponse("Failed to Load Data {}".format(r))