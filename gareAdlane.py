# from os import O_SEQUENTIAL, write
from pprint import pprint
import json
import requests
import os


currentDirectory = os.getcwd()

print(currentDirectory)


# url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
# token_auth = '5467e28e-385b-4f3c-8bbd-8a5c4d9f3b38'
# token_password = ''
# r = requests.get(url, auth=(token_auth, token_password))


# raw_data2 = r.json()

# list_journeys = []
# data_json = r.json()['journeys']

# for i in data_json:
#     if type(i) == dict:
#         dict_journeys = {}
#         if 'sections' in i.keys():
#             dict_journeys['sections'] = i['sections']
#             for e in i['sections']:

#                 if 'stop_date_time' in e['to'].keys():
#                     print("VOILE LE >E", e['to']['stop_date_times'])
#                 else:
#                     print('pas de stop_date_time')
            
#                 if 'stop_point' in e['to'].keys():
#                     print('Valeur de stop_point : ', e['to']['stop_point'])
#                 else:
#                     print('pas de stop_point')


#             # i['section'][Ø]['to']['stop_point'] ??
#         else: 
#             print('no')
#         list_journeys.append(dict_journeys)
#         dict_journeys = {}

# pprint(list_journeys)





# def searchStation(to, from):
#     url = journeysUrl
#     api_key = token_auth
#     destination1 = from
#     destination2 = to
#     final_url =  url + "?from" + destination1 + "&to" + destination2

#     for item in raw_data: