import requests
from dotenv import load_dotenv
import os
load_dotenv()


class GoogleMaps:
    def __init__(self):
        pass

    @staticmethod
    def calcDistance(cityA, cityB):
        route = requests.get(f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={cityA}&origins={cityB}&key={os.getenv('GOOGLE_MAPS_API_KEY')}")

        distanceString = route.json().get('rows')[0].get('elements')[0].get('distance').get('value')
        distance = int(distanceString) / 1000
        return distance
if __name__ == '__main__':
    GoogleMaps.calcDistance('Krakow', 'Paris')