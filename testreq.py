import requests
import json


# def makeRequest(url, headers=None, params=None):
#     return requests.get(url=url, headers=headers, params=params)

# def newLine():
#     print("\n\n\n\n\n\n\n\n")

# api_key = "_9lSdEylcyUrURMdo0RU4tmV3wmvco0MXaWBk3mcxomqoZShLXPcl1YZOfg-4qHKDVXFZeIPPRIbPZdv8LeHoKPVDGNV90wULEey0tMdHVphlHhpV_sBAsoFHfknW3Yx"
# api_host = "https://api.yelp.com/v3/businesses/search"


# term = 'dinner'
# location = 'San Francisco, CA'
# SEARCH_LIMIT = 3

# headers = {
#     'Authorization': 'Bearer %s' % api_key,
# }

# url_params = {
#     'term': term.replace(' ', '+'),
#     'latitude': 34.00,
#     'longitude' : -118.0145,
#     'limit': SEARCH_LIMIT
# }


# # response = makeRequest(api_host, headers=headers, params=url_params)
# # print(response.json())

# newLine()
# #here api
# app_id = "kNmRfgEIQXC5FYzw5tLL"
# app_code = "ZAsalDdtJQp0p3bi4uJJzg"

# baseUrl = "https://route.cit.api.here.com/routing/7.2/calculateroute.json"
# url_params = {
#     "app_id" : app_id,
#     "app_code" : app_code,
#     "waypoint0" : "40.7163,-74.0123",
#     "waypoint1" : "33.718803,-117.789083",
#     "mode" : "fastest;car;traffic:enabled;motorway:-2",
#     "departure" : "now"

# }

# response = makeRequest(baseUrl, headers=None, params=url_params)
# print(response.json())
# newLine()
# response = makeRequest("{}?app_id={}&app_code={}&product={}&name={}".format(
#     baseUrl, 
#     url_params["app_id"], 
#     url_params["app_code"], 
#     url_params["product"],
#     url_params["name"]
#     ))

# print(response.json())
# newLine()
# baseUrl = "https://route.cit.api.here.com/routing/7.2/calculateroute.json?app_id={}&app_code={}&waypoint0=geo!52.5,13.4&waypoint1=geo!30.5,13.45&mode=fastest;car;traffic:enabled".format(
#     url_params["app_id"], 
#     url_params["app_code"], 
# )


# response = makeRequest(baseUrl, headers=None, params=None)
# print(response.json())


data = {
  "response": {
    "metaInfo": {
      "timestamp": "2018-06-23T05:53:17Z",
      "mapVersion": "8.30.84.156",
      "moduleVersion": "7.2.201824-28929",
      "interfaceVersion": "2.6.34",
      "availableMapVersion": [
        "8.30.84.156"
      ]
    },
    "route": [
      {
        "waypoint": [
          {
            "linkId": "-826632453",
            "mappedPosition": {
              "latitude": 52.5162041,
              "longitude": 13.378365
            },
            "originalPosition": {
              "latitude": 52.5159999,
              "longitude": 13.3778999
            },
            "type": "stopOver",
            "spot": 0.5384615,
            "sideOfStreet": "right",
            "mappedRoadName": "Pariser Platz",
            "label": "Pariser Platz",
            "shapeIndex": 0
          },
          {
            "linkId": "+722940051",
            "mappedPosition": {
              "latitude": 52.5206638,
              "longitude": 13.3861149
            },
            "originalPosition": {
              "latitude": 52.5205999,
              "longitude": 13.3861999
            },
            "type": "stopOver",
            "spot": 0.4634146,
            "sideOfStreet": "right",
            "mappedRoadName": "Reichstagufer",
            "label": "Reichstagufer",
            "shapeIndex": 14
          }
        ],
        "mode": {
          "type": "fastest",
          "transportModes": [
            "car"
          ],
          "trafficMode": "enabled",
          "feature": []
        },
        "leg": [
          {
            "start": {
              "linkId": "-826632453",
              "mappedPosition": {
                "latitude": 52.5162041,
                "longitude": 13.378365
              },
              "originalPosition": {
                "latitude": 52.5159999,
                "longitude": 13.3778999
              },
              "type": "stopOver",
              "spot": 0.5384615,
              "sideOfStreet": "right",
              "mappedRoadName": "Pariser Platz",
              "label": "Pariser Platz",
              "shapeIndex": 0
            },
            "end": {
              "linkId": "+722940051",
              "mappedPosition": {
                "latitude": 52.5206638,
                "longitude": 13.3861149
              },
              "originalPosition": {
                "latitude": 52.5205999,
                "longitude": 13.3861999
              },
              "type": "stopOver",
              "spot": 0.4634146,
              "sideOfStreet": "right",
              "mappedRoadName": "Reichstagufer",
              "label": "Reichstagufer",
              "shapeIndex": 14
            },
            "length": 905,
            "travelTime": 261,
            "maneuver": [
              {
                "position": {
                  "latitude": 52.5162041,
                  "longitude": 13.378365
                },
                "instruction": "Head <span class=\"heading\">east</span> on <span class=\"street\">Pariser Platz</span>. <span class=\"distance-description\">Go for <span class=\"length\">80 m</span>.</span>",
                "travelTime": 60,
                "length": 80,
                "id": "M1",
                "_type": "PrivateTransportManeuverType"
              },
              {
                "position": {
                  "latitude": 52.5162792,
                  "longitude": 13.3795345
                },
                "instruction": "Continue on <span class=\"next-street\">Unter den Linden</span>. <span class=\"distance-description\">Go for <span class=\"length\">90 m</span>.</span>",
                "travelTime": 78,
                "length": 90,
                "id": "M2",
                "_type": "PrivateTransportManeuverType"
              },
              {
                "position": {
                  "latitude": 52.5163651,
                  "longitude": 13.3808541
                },
                "instruction": "Turn <span class=\"direction\">left</span> onto <span class=\"next-street\">Wilhelmstraße</span>. <span class=\"distance-description\">Go for <span class=\"length\">288 m</span>.</span>",
                "travelTime": 50,
                "length": 288,
                "id": "M3",
                "_type": "PrivateTransportManeuverType"
              },
              {
                "position": {
                  "latitude": 52.5189292,
                  "longitude": 13.3802962
                },
                "instruction": "Turn <span class=\"direction\">right</span> onto <span class=\"next-street\">Reichstagufer</span>. <span class=\"distance-description\">Go for <span class=\"length\">447 m</span>.</span>",
                "travelTime": 73,
                "length": 447,
                "id": "M4",
                "_type": "PrivateTransportManeuverType"
              },
              {
                "position": {
                  "latitude": 52.5206638,
                  "longitude": 13.3861149
                },
                "instruction": "Arrive at <span class=\"street\">Reichstagufer</span>. Your destination is on the right.",
                "travelTime": 0,
                "length": 0,
                "id": "M5",
                "_type": "PrivateTransportManeuverType"
              }
            ]
          }
        ],
        "summary": {
          "distance": 905,
          "trafficTime": 261,
          "baseTime": 260,
          "flags": [
            "noThroughRoad",
            "builtUpArea"
          ],
          "text": "The trip takes <span class=\"length\">905 m</span> and <span class=\"time\">4 mins</span>.",
          "travelTime": 261,
          "_type": "RouteSummaryType"
        }
      }
    ],
    "language": "en-us"
  }
}

print(type(data))
print(data['response']['route'][0]['summary'])