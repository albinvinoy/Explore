from django.shortcuts import render, HttpResponse, get_object_or_404
import requests
from .accessKey import *
import json, random, timeit
# Create your views here.

#main - make request
def makeRequest(url, params=None, headers=None):
    response = requests.get(url, headers=headers, params=params)
    return response

# access the ipstack to get geo location
def getGeoCoordinates():
    return [34.0522, -118.2437]
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
        # #print("Failed to get response")
        return [34.0522, -118.2437] #default to LA

#here maps api

def tripDetails(ocord, dcord):
    baseUrl = "https://route.cit.api.here.com/routing/7.2/calculateroute.json"
    url_params = {
        "app_id" : HERE_API_ID,
        "app_code" : HERE_APP_CODE,
        "waypoint0" : "{},{}".format( ocord[0], ocord[1] ),
        "waypoint1" : "{},{}".format( dcord[0], dcord[1] ),
        "mode" : "fastest;car;traffic:enabled;motorway:-2",
        "departure" : "now"
    }

    response = makeRequest(baseUrl, params=url_params)
    #print(response + 'here api')
    if response.status_code == 200:
        # #print(response.json()['response']['route'][0]['summary'])
        return response.json()['response']['route'][0]['summary']
    else:
        return None
#yelp api helper

def formatYelpData(jsonData):
    finalData = []
    for x in jsonData["businesses"]:
        temp = {}
        destCoord = [x["coordinates"]["latitude"], x["coordinates"]["longitude"]]
        temp["origin"] = getGeoCoordinates()
        temp["destination"] = destCoord
        temp["title" ]= x["name"]
        temp["rating" ]= x["rating"]
        temp["open" ]= x["is_closed"]
        temp["number" ]=x["display_phone"]
        temp["image" ]= x["image_url"]
        temp["reviews" ]= x["review_count"]
        temp["url"] = x["url"]
        temp["address" ]= ' '.join(x["location"]["display_address"])
        temp["tripDetails"] = tripDetails(getGeoCoordinates(),destCoord)

        finalData.append(temp)
    #print(finalData + 'massage data')

    return finalData


def getYelpInfo(keyword="", coordinates=[]):
    term = keyword or "dinner" # get from form
    SEARCH_LIMIT = 6 # 10 as default
    url = "https://api.yelp.com/v3/businesses/search"

    headers = {
        'Authorization': 'Bearer %s' % YELP_API_KEY,
    }

    url_params = {
        'term': term.replace(' ', '+'),
        'latitude': coordinates[0],
        'longitude' : coordinates[1],
        'limit': SEARCH_LIMIT,
        'open_now' : True
    }

    response = makeRequest(url=url, params=url_params, headers=headers)
    #print(response + 'yelp call')
    return response

#main view functions
def index(request):
    # getGeoCoordinates() = getGeoCoordinates()
    r = ['food', 'dessert', 'outdoor', 'nightlife', 'concert', 'theater', 'parks', 'zoo','hospitals']
    #print('{} {}'.format(r, "index"))
    return render(request, 'exploree/index.html', context={"titles" : r })


# def food(request):
#     r = getYelpInfo('american food', getGeoCoordinates())
#     if r.status_code==200:
#         r = formatYelpData(r.json())
#         return render(request, 'exploree/yelp.html', context={'raw_data':r})
#     else:
#         return HttpResponse("Failed to Load Data {}".format(r))

# def activitites(request):
#     r = getYelpInfo('activities', getGeoCoordinates())
#     if r.status_code==200:
#         r = formatYelpData(r.json())
#         return render(request, 'exploree/yelp.html', context={'raw_data':r})
#     else:
#         return HttpResponse("Failed to Load Data {}".format(r))


def whatTodo(request, whatTodo):
    start = timeit.default_timer()
    r = getYelpInfo(whatTodo, getGeoCoordinates())
    #print(r + "whattodo")
    if r.status_code==200:
        r = formatYelpData(r.json())
        print(timeit.default_timer() - start)
        return render(request, 'exploree/yelp.html', context={'raw_data':r})
    else:
        print(timeit.default_timer() - start)        
        return HttpResponse("Failed to Load Data {}".format(r))