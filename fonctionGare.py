from pprint import pprint
import csv
import json
import requests
import os


currentDirectory = os.getcwd()
token_auth = '2da277f8-8a43-49f3-9468-5f32fbbed6e7'
url_api = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'
request_api_sncf = requests.get(url_api, auth=(token_auth, ''))
data = request_api_sncf.json()['stop_areas']
list_gares = []


def create_csv_inside_function(data_gare, entete_colonnes):
    try:
        # Create csv file
        with open(currentDirectory + '/stop_areas.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=entete_colonnes)
            writer.writeheader()
            for data in data_gare:
                writer.writerow(data)
    except IOError:
        print("I/O error")

# Pour récupérer les données de l'api


def createCSV(data):
    for loop_area in data:
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
            list_gares.append(dict_gare)
            dict_gare = {}
        else:
            print(f'Unexpected format {type(loop_area)}')
    pprint(list_gares)
    # Fin:  Pour récupérer les données de l'api

    # Pour créer le fichier csv
    csv_columns = []

    for element in list_gares:
        if all(el in element for el in ('id', 'coord', 'name', 'admin_region_id', 'admin_region_name', 'admin_region_zip_code', 'admin_region_insee')):
            csv_columns = [i for i in element.keys()]
            break

    create_csv_inside_function(list_gares, csv_columns)
    # Fin: Pour créer le fichier csv
createCSV(data)
