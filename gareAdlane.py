# from os import O_SEQUENTIAL, write
from pprint import pprint
import json
import requests
import os
import csv


class APIJourneys():

    def __init__(self):
        self.url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
        self.token = '5467e28e-385b-4f3c-8bbd-8a5c4d9f3b38'
        self.file_name_export_journeys = 'journeys'
        self.request_api_sncf = None
        self.list_stops = []
        self.list_header_columns =[]

    def get_header_columns(self):
        for element in self.list_stops:
            if all(el in element for el in ('arrival_date_time', 'departure_date_time')):
                self.list_header_columns = [i for i in element.keys()]

    def create_csv(self):
        try:
            self.get_header_columns()
            with open(os.getcwd() + '/' + self.file_name_export_journeys + '.csv', 'w') as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=self.list_header_columns)
                writer.writeheader()
                for data in self.list_stops:
                    writer.writerow(data)
        except IOError:
            print("I/O error")

    def read_url_journeys(self, url_journeys):
        res = requests.get(url_journeys, auth=(self.token, ''))
        if res.status_code == 200:
            with open(os.getcwd() + '/' + self.file_name_export_journeys + '.json', 'w') as JsonFile:
                json.dump(res.json(), JsonFile, indent=4)
        else:
            print('json not created')

    
    def get_data_from_json(self):
        with open(os.getcwd() + '/' + self.file_name_export_journeys + '.json') as json_file:
            self.request_api_sncf = json.load(json_file)

    def get_stops(self, journeysStopPoint):
        for loop_journeys in journeysStopPoint:
            if type(loop_journeys) == dict:
                dict_journeys = {}
                if 'arrival_date_time' in loop_journeys.keys():
                    dict_journeys['arrival_date_time'] = loop_journeys['arrival_date_time']
                else:
                    print('missing : arrival_date_time')

                if 'departure_date_time' in loop_journeys.keys():
                        dict_journeys['departure_date_time'] = loop_journeys['departure_date_time']
                else:
                    print('missing : departure_date_time')


                if 'requested_date_time' in loop_journeys.keys():
                        dict_journeys['requested_date_time'] = loop_journeys['requested_date_time']
                else:
                    print('missing : requested_date_time')

                if 'sections' in loop_journeys.keys():
                    ad_section_data = loop_journeys['sections'][0]
                    dict_journeys['from'] = ad_section_data['from']
                else:
                    print('missing key administrative region')

                self.list_stops.append(dict_journeys)
                dict_journeys ={}
            else: 
                print(f'unexpected format {type(loop_journeys)}')
                
                


my_test_journeys = APIJourneys()
my_test_journeys.read_url_journeys(my_test_journeys.url)
my_test_journeys.get_data_from_json()
all_journeys = my_test_journeys.request_api_sncf['journeys']
my_test_journeys.get_stops(all_journeys)
my_test_journeys.create_csv()






    # def get_all_journeys(self, data):
    #     for i in self.data:
    #         if type(i) == dict:
    #             dict_journeys = {}
    #             if 'sections' in i.keys():
    #                 dict_journeys['sections'] = i['sections']
    #                 for e in i['sections']:

    #                     if 'stop_date_time' in e['to'].keys():
    #                         print("VOILE LE >E", e['to']['stop_date_times'])
    #                     else:
    #                         print('pas de stop_date_time')
                    
    #                     if 'stop_point' in e['to'].keys():
    #                         print('Valeur de stop_point : ', e['to']['stop_point'])
    #                     else:
    #                         print('pas de stop_point')
    #             else: 
    #                 print('no') 
    #             list_journeys.append(dict_journeys)
    #             dict_journeys = {}






# def searchStation(to, from):
#     url = journeysUrl
#     api_key = token_auth
#     destination1 = from
#     destination2 = to
#     final_url =  url + "?from" + destination1 + "&to" + destination2

#     for item in raw_data:
