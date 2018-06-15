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
    SEARCH_LIMIT = 20 # 10 as default
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
    r =  [{'title': 'Six Taste', 'url': 'https://www.yelp.com/biz/six-taste-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 619, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/LDVzcytjxD1yf1tIoX58Pw/o.jpg', 'number': '(213) 798-4749', 'address': 'Los Angeles, CA 90015', 'rating': 5.0, 'open': False}, {'title': 'The Broad', 'url': 'https://www.yelp.com/biz/the-broad-los-angeles-4?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 1898, 'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/Pl86Cvz_5dNfQYXSkxiD5A/o.jpg', 'number': '(213) 232-6200', 'address': '221 S Grand Ave Los Angeles, CA 90012', 'rating': 4.0, 'open': False}, {'title': 'Grand Park', 'url': 'https://www.yelp.com/biz/grand-park-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 333, 'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/BmcsMcThhyebXTIM9wb2Pw/o.jpg', 'number': '(213) 972-8080', 'address': '200 N Grand Ave Los Angeles, CA 90012', 'rating': 4.5, 'open': False}, {'title': 'Maze Rooms Escape Game', 'url': 'https://www.yelp.com/biz/maze-rooms-escape-game-los-angeles-8?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 416, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/GVRTeZcPXEQwdk1RkogvCg/o.jpg', 'number': '(323) 497-9776', 'address': '132 S Vermont Ave Ste 204 Los Angeles, CA 90004', 'rating': 5.0, 'open': False}, {'title': 'Echo Park Boats by Wheel Fun Rentals', 'url': 'https://www.yelp.com/biz/echo-park-boats-by-wheel-fun-rentals-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 95, 'image': 'https://s3-media4.fl.yelpcdn.com/bphoto/2rJQbRlC9J9bi8gzm9N1nQ/o.jpg', 'number': '(805) 650-7770', 'address': '751 Echo Park Ave Los Angeles, CA 90026', 'rating': 4.5, 'open': False}, {'title': 'California Science Center', 'url': 'https://www.yelp.com/biz/california-science-center-los-angeles-5?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 1266, 'image': 'https://s3-media1.fl.yelpcdn.com/bphoto/E8iGc7tcEHH8q77Ek0zGug/o.jpg', 'number': '(323) 724-3623', 'address': '700 Exposition Park Dr Los Angeles, CA 90037', 'rating': 4.0, 'open': False}, {'title': 'lazRfit', 'url': 'https://www.yelp.com/biz/lazrfit-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 80, 'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/c8vUqmZAT26GKy4csNbCfA/o.jpg', 'number': '(855) 529-7348', 'address': '400 W Pico Blvd Los Angeles, CA 90015', 'rating': 5.0, 'open': False}, {'title': 'Griffith Observatory', 'url': 'https://www.yelp.com/biz/griffith-observatory-los-angeles-2?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 2990, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/U-R5eIaZPBRUQst6Lv8Evg/o.jpg', 'number': '(213) 473-0800', 'address': '2800 E Observatory Rd Los Angeles, CA 90027', 'rating': 4.5, 'open': False}, {'title': 'Escape Room LA', 'url': 'https://www.yelp.com/biz/escape-room-la-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 304, 'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/ZD_awUqpkBBrzxIJaIRn1A/o.jpg', 'number': '(213) 689-3229', 'address': '120 E 8th St Los Angeles, CA 90014', 'rating': 4.5, 'open': False}, {'title': 'CicLAvia', 'url': 'https://www.yelp.com/biz/ciclavia-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 170, 'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/JuD7PgZQym_XgIkXXSeV2A/o.jpg', 'number': '(213) 355-8500', 'address': '525 S Hewitt St Los Angeles, CA 90013', 'rating': 4.5, 'open': False}, {'title': 'OUE Skyspace LA', 'url': 'https://www.yelp.com/biz/oue-skyspace-la-los-angeles-2?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 607, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/Ep19tW6Q45eDvTJdLBW0eA/o.jpg', 'number': '(213) 894-9000', 'address': '633 W Fifth St Fl 2 Los Angeles, CA 90071', 'rating': 3.5, 'open': False}, {'title': 'LA Boulders', 'url': 'https://www.yelp.com/biz/la-boulders-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 151, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/Yi3ntcXTqmoQ9Iv8iBSZCg/o.jpg', 'number': '(323) 406-9119', 'address': '1375 E 6th St Unit 8 Los Angeles, CA 90021', 'rating': 4.5, 'open': False}, {'title': 'Japanese American National Museum', 'url': 'https://www.yelp.com/biz/japanese-american-national-museum-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 316, 'image': 'https://s3-media1.fl.yelpcdn.com/bphoto/B2iGc1ExbjTBcWY5MBfY7w/o.jpg', 'number': '(213) 625-0414', 'address': '100 N Central Ave Los Angeles, CA 90012', 'rating': 4.5, 'open': False}, {'title': 'Virtual Reality Games', 'url': 'https://www.yelp.com/biz/virtual-reality-games-los-angeles-3?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 27, 'image': 'https://s3-media2.fl.yelpcdn.com/bphoto/wzHfkDMEdbi8qGjYSLO1qA/o.jpg', 'number': '(323) 999-5342', 'address': '6519 Hollywood Blvd Los Angeles, CA 90028', 'rating': 5.0, 'open': False}, {'title': 'LA River Expeditions', 'url': 'https://www.yelp.com/biz/la-river-expeditions-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 58, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/CKfrMQVX-a0Pxvxlzdb4gw/o.jpg', 'number': '(323) 392-4247', 'address': 'Los Angeles, CA 90039', 'rating': 4.5, 'open': False}, {'title': 'LA Cycle Tours', 'url': 'https://www.yelp.com/biz/la-cycle-tours-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 28, 'image': 'https://s3-media4.fl.yelpcdn.com/bphoto/YKG-OpkWuQT0i4lPkMGK4w/o.jpg', 'number': '(323) 550-8265', 'address': 'Los Angeles, CA 90042', 'rating': 5.0, 'open': False}, {'title': 'Sidewalk Food Tours of Los Angeles', 'url': 'https://www.yelp.com/biz/sidewalk-food-tours-of-los-angeles-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 59, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/2sLlFZEwdUdrLABY66_sqg/o.jpg', 'number': '(877) 568-6877', 'address': '545 S Olive St Los Angeles, CA 90013', 'rating': 5.0, 'open': False}, {'title': 'City of Los Angeles', 'url': 'https://www.yelp.com/biz/city-of-los-angeles-los-angeles-38?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 127, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/4_royq5_hGRjCgsWxzFgsw/o.jpg', 'number': '(213) 473-5901', 'address': '200 N Spring St Ste 101 Los Angeles, CA 90012', 'rating': 3.5, 'open': False}, {'title': 'Urban LA Boot Camp', 'url': 'https://www.yelp.com/biz/urban-la-boot-camp-los-angeles?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 41, 'image': 'https://s3-media4.fl.yelpcdn.com/bphoto/ePrKv-Uuz-gBs_BWPddmdA/o.jpg', 'number': '(213) 280-7577', 'address': '255 S Grand Ave Los Angeles, CA 90012', 'rating': 5.0, 'open': False}, {'title': 'Maze Rooms', 'url': 'https://www.yelp.com/biz/maze-rooms-los-angeles-17?adjust_creative=n3l2L60BFLktWAtI78TO8w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=n3l2L60BFLktWAtI78TO8w', 'reviews': 251, 'image': 'https://s3-media3.fl.yelpcdn.com/bphoto/scGYDWbJgrxDwlUSYuhlUQ/o.jpg', 'number': '(310) 595-2881', 'address': '1182 S La Brea Ave Los Angeles, CA 90019', 'rating': 4.5, 'open': False}]
    return render(request, 'exploree/activities.html', context={'raw_data':r})
    
    r = getYelpInfo('activities', getGeoCoordinates())
    if r.status_code==200:
        r = formatYelpData(r.json())
        return render(request, 'exploree/activities.html', context={'raw_data':r})
    else:
        return HttpResponse("Failed to Load Data {}".format(r))