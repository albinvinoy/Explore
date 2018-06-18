from django.shortcuts import render, HttpResponse
import requests
# Create your views here.

def index(request):
    getGeoCoordinates()
    return HttpResponse("well you are not watching the index")

    
# access the ipstack to get geo location
def getGeoCoordinates():
    GEO_ACCESS_KEY = "6355c5c7edec3cf8b5f6de9d705ccc78"
    baseUrl = "http://api.ipstack.com/check?access_key={}&security=1&fields=main".format(GEO_ACCESS_KEY)
    response = requests.get(baseUrl)
    if response.status_code == 200:
        data = response.json()
        print(data["latitude"], data["longitude"])
        return []
    else:
        print("Failed to get response")


#eventbrite access key
def getAccessToken():
    EVENT_BRITE_CLIENT_SECRET = "3E2P56WVY6EJFMJYTSC7ENJ7O2BLIXVALARWPZWZV5R4I2NJIT"
    EVENT_BRITE_OAUTH_TOKEN = "U6GJEWKANSLQBDDNHR2Z"
    