#!/usr/bin/env python3

import requests
import json
import csv
import logging
from pprint import pprint
import os

logging.basicConfig(filename=os.getcwd()+"/log.txt", filemode="w", format="%(asctime)s -  %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG)

url_api = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'
token_auth = '2da277f8-8a43-49f3-9468-5f32fbbed6e7'



def get_header_columns(data_list_gares):
    for element in data_list_gares:
        if all(el in element for el in ('id', 'coord', 'name', 'admin_region_id', 'admin_region_name', 'admin_region_zip_code', 'admin_region_insee')):
            return [i for i in element.keys()]


def create_csv(data_gare):
    try:
        entete_colonnes = get_header_columns(data_gare)
        # Create csv file
        with open(os.getcwd() + '/stop_areas.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=entete_colonnes)
            writer.writeheader()
            for data in data_gare:
                writer.writerow(data)
    except IOError: 
        logging.info("I/O error")


def read_json(url_test):
    request_api = requests.get(url_test, auth=(token_auth, ''))
    if request_api.status_code == 200:
        with open(os.getcwd() + '/stop_areas.json', 'w') as outfile:
            json.dump(request_api.json(), outfile, indent=4)
    else:
        print('request Not found')


# function get data from json file
# get and read json file
def get_data_from_json():
    with open(os.getcwd() + '/stop_areas.json') as json_file:
        myDictJson = json.load(json_file)
    return myDictJson

read_json(url_api)

request_api_sncf = get_data_from_json()

all_areas = request_api_sncf['stop_areas']


def get_all_areas(areas):
    list_gares_origin = []
    for loop_area in areas:
        if type(loop_area) == dict:
            dict_gare = {}
            if 'id' in loop_area.keys():
                dict_gare['id'] = loop_area['id']
            else:
                print('missing key id')

            if 'coord' in loop_area.keys():
                dict_gare['coord'] = loop_area['coord']
            else:
                print('missing key coord')

            if 'name' in loop_area.keys():
                dict_gare['name'] = loop_area['name']
            else:
                print('missing key name')

            if 'administrative_regions' in loop_area.keys():
                ad_region_data = loop_area['administrative_regions'][0]
                dict_gare['admin_region_id'] = ad_region_data['id']
                dict_gare['admin_region_name'] = ad_region_data['name']
                dict_gare['admin_region_zip_code'] = ad_region_data['zip_code']
                dict_gare['admin_region_insee'] = ad_region_data['insee']
            else:
                print('missing key administrative region')

            list_gares_origin.append(dict_gare)
            dict_gare = {}
        else:
            print(f'Unexpected format {type(loop_area)}')
    return list_gares_origin


list_gares = get_all_areas(all_areas)

create_csv(list_gares)
