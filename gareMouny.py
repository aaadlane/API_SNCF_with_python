from pprint import pprint
import csv
import json
import requests


url_api = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'

token_auth = '2da277f8-8a43-49f3-9468-5f32fbbed6e7'

request_api_sncf = requests.get(url_api, auth=(token_auth, ''))

areas = request_api_sncf.json()['stop_areas']

# Pour récupérer les données de l'api
list_gares = []

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

try:
    # Create csv file
    with open('stop_areas.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in list_gares:
            writer.writerow(data)
except IOError:
    print("I/O error")
# Fin: Pour créer le fichier csv
