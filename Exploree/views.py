from django.shortcuts import render, HttpResponse
import requests
from .accessKey import GEO_ACCESS_KEY, YELP_API_KEY
# Create your views here.

def index(request):
    print(getGeoCoordinates())
    return render(request, 'exploree/index.html')


def food(request):
    return HttpResponse("This is food page")
    
# access the ipstack to get geo location
def getGeoCoordinates():
    baseUrl = "http://api.ipstack.com/check?access_key={}&security=1&fields=main".format(GEO_ACCESS_KEY)
    response = requests.get(baseUrl)
    if response.status_code == 200:
        data = response.json()
        return [data["latitude"], data["longitude"]]
    else:
        print("Failed to get response")
    return [34.0522, 118.2437] #default to LA

#yelp api
def requestYelpData(url, searchTerms, urlParams):
    pass