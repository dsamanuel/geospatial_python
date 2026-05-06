import requests
import time
import os
import json
from dotenv import load_dotenv


#calculating distance between two points on the Earth’s surface can be done using different formulae. The most common ones are the Haversine formula, the Vincenty formula, and the Great Circle distance. Each of these formulae has its own advantages and disadvantages, and the choice of which one to use depends on the specific use case and the level of accuracy required.
# Build paths inside the project like this: BASE_DIR / 'subdir'.




load_dotenv()  
ORS_API_KEY = os.getenv('API_KEY')

def get_driving_distance(source_coordinates, dest_coordinates):
    parameters = {
    'api_key': ORS_API_KEY,
    'start' : '{},{}'.format(source_coordinates[1], source_coordinates[0]),
    'end' : '{},{}'.format(dest_coordinates[1], dest_coordinates[0])
    }

    response = requests.get(
        'https://api.openrouteservice.org/v2/directions/driving-car', params=parameters)

    if response.status_code == 200:
        data = response.json()
        summary = data['features'][0]['properties']['summary']
        distance = summary['distance']
        return distance/1000
    else:
        print('Request failed.')
        print('Reason', response.text) 
        return -9999

san_francisco = (37.7749, -122.4194)

destination_cities = {
    'Los Angeles': (34.0522, -118.2437),
    'Boston': (42.3601, -71.0589),
    'Atlanta': (33.7490, -84.3880)
}

get_driving_distance(san_francisco, destination_cities['Los Angeles'])