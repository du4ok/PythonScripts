import json
import csv
import requests
from pprint import pprint

BASE_URL = 'http://maps.googleapis.com/maps/api/geocode/json?address='
#city = 'yahotyn'

def get_city_url(city):
    return BASE_URL + str(city)

def get_json_data(url):
    json_data = requests.get(url).json()
    pprint(json_data['results'][0]['address_components'])

def main():
    l = ['Kiev','Yahotyn','Madrid','Chicago']
    for city in l:
        get_json_data(get_city_url(city))

if __name__ == '__main__':
    main()


