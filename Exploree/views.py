from django.shortcuts import render, HttpResponse, get_object_or_404
import requests
from .accessKey import GEO_ACCESS_KEY, YELP_API_KEY
import json
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
        # print("Failed to get response")
        return [34.0522, -118.2437] #default to LA

#yelp api helper

def formatYelpData(jsonData):
    finalData = []
    for x in jsonData["businesses"]:
        temp = {}
        temp["title" ]= x["name"]
        temp["rating" ]= x["rating"]
        temp["open" ]= x["is_closed"]
        temp["number" ]=x["display_phone"]
        temp["image" ]= x["image_url"]
        temp["reviews" ]= x["review_count"]
        temp["url"] = x["url"]
        temp["address" ]= ' '.join(x["location"]["display_address"])

        finalData.append(temp)

    return finalData


def getYelpInfo(keyword="", coordinates=[]):
    term = keyword or "dinner" # get from form
    SEARCH_LIMIT = 5 # 10 as default
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
    return response


#main view functions
def index(request):
    return render(request, 'exploree/index.html')


def food(request):
    r = getYelpInfo('dinner', getGeoCoordinates())
    if r.status_code==200:
        return render(request, 'exploree/food.html', context={'raw_data':r.json() })
    else:
        return HttpResponse("Failed to Load Data {}".format(r))

def activitites(request):
    # r = [{'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/JuD7PgZQym_XgIkXXSeV2A/o.jpg', 'open': False, 'number': '(213) 355-8500', 'reviews': 'https://s3-media2.fl.yelpcdn.com/bphoto/JuD7PgZQym_XgIkXXSeV2A/o.jpg', 'title': 'CicLAvia', 'address': ['525 S Hewitt St', 'Los Angeles, CA 90013'], 'rating': 4.5}, {'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/zUCVuAlCD-qev1ATDZWDmA/o.jpg', 'open': False, 'number': '(323) 252-4597', 'reviews': 'https://s3-media3.fl.yelpcdn.com/bphoto/zUCVuAlCD-qev1ATDZWDmA/o.jpg', 'title': 'Battle For LA', 'address': ['Los Angeles, CA 90291'], 'rating': 5.0}]
    # return render(request, 'exploree/activities.html', context={'raw_data':r})
    
    r = getYelpInfo('activities', getGeoCoordinates())
    if r.status_code==200:
        r = formatYelpData(r.json())
        return render(request, 'exploree/activities.html', context={'raw_data':r})
    else:
        return HttpResponse("Failed to Load Data {}".format(r))