# Calculating Distance
# Required package: geopy
# geopy comes with functions that have already implemented many distance calculation formulae.


from geopy import distance
import requests

import os
import json
from dotenv import load_dotenv


#Calculating distance between two points on the Earth’s surface can be done using different formulae. The most common ones are the Haversine formula, the Vincenty formula, and the Great Circle distance. Each of these formulae has its own advantages and disadvantages, and the choice of which one to use depends on the specific use case and the level of accuracy required.
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  
san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)

straight_line_distance = distance.great_circle(san_francisco, new_york)
ellipsoid_distance = distance.geodesic(san_francisco, new_york, ellipsoid='WGS-84')

print(straight_line_distance, ellipsoid_distance)




san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)

parameters = {
    'api_key': os.getenv('API_KEY'),
    'start' : '{},{}'.format(san_francisco[1], san_francisco[0]),
    'end' : '{},{}'.format(new_york[1], new_york[0])
}

response = requests.get('https://api.openrouteservice.org/v2/directions/driving-car', params=parameters)
