import requests
import json
import csv
from pprint import pprint
import os


class ApiSncf:
    def __init__(self):
        self.url_api = 'https://api.sncf.com/v1/coverage/sncf/stop_areas'
        self.token_auth = '2da277f8-8a43-49f3-9468-5f32fbbed6e7'
        self.filename_export = 'stop_areas'
        self.request_api_sncf = None
        self.list_gares = []
        self.list_header_columns = []

    def get_header_columns(self):
        for element in self.list_gares:
            if all(el in element for el in ('id', 'coord', 'name', 'admin_region_id', 'admin_region_name', 'admin_region_zip_code', 'admin_region_insee')):
                self.list_header_columns = [i for i in element.keys()]

    def create_csv(self):
        try:
            self.get_header_columns()
            with open(os.getcwd() + '/' + self.filename_export + '.csv', 'w') as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=self.list_header_columns)
                writer.writeheader()
                for data in self.list_gares:
                    writer.writerow(data)
        except IOError:
            print("I/O error")

    def read_url_json(self, url_test):
        request_api = requests.get(url_test, auth=(self.token_auth, ''))
        if request_api.status_code == 200:
            with open(os.getcwd() + '/' + self.filename_export + '.json', 'w') as outfile:
                json.dump(request_api.json(), outfile, indent=4)
        else:
            print('request Not found')

    def get_data_from_json(self):
        with open(os.getcwd() + '/' + self.filename_export + '.json') as json_file:
            self.request_api_sncf = json.load(json_file)

    def get_all_areas(self, areas):
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

                self.list_gares.append(dict_gare)
                dict_gare = {}
            else:
                print(f'Unexpected format {type(loop_area)}')


my_test_areas = ApiSncf()
my_test_areas.read_url_json(my_test_areas.url_api)
my_test_areas.get_data_from_json()
all_areas = my_test_areas.request_api_sncf['stop_areas']
my_test_areas.get_all_areas(all_areas)
my_test_areas.create_csv()
