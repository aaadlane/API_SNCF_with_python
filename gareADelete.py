# from os import O_SEQUENTIAL, write
from pprint import pprint
import json
import requests
import csv
import urllib

# https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025

# url = "https://api.sncf.com/v1/coverage/sncf/stop_areas/"
url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
token_auth = '5467e28e-385b-4f3c-8bbd-8a5c4d9f3b38'
token_password = ''
r = requests.get(url, auth=(token_auth, token_password))
raw_data = json.loads(r.text)
text_json = json.dumps(raw_data)

journeysUrl = 'https://api.sncf.com/v1/coverage/sncf/journeys/'
journeys_request = requests.get(journeysUrl, auth=(token_auth, token_password))
journeys_data = json.loads(journeys_request.text)
# pprint(r.json())
# pprint(r.json()['journeys'])

list_journeys = []
raw_data2 = r.json()
data_json = r.json()['journeys']



def get_json(data, i=0):
    i += 1
    if type(data) == dict:
        for key, value in dict(data).items():
            print("    "*(i-1)+"|--->", key, 'dict')
            get_json(value,i)
    elif type(data) == list:
        print("list")
        if len(list(data)) > 0:
            get_json(list(data)[0],i)

print(get_json(raw_data))

# print(raw_data2)
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









# journeys = "journeys": [{"sections": [{"stop_date_times": [{"stop_point": {"name: 'gare de lyon'}}]}]}]

# with open('./test.json', 'w') as outfile:
#     json.dump(r.json(), outfile, indent=4)

# for i in r.json():
#     print(i)

# pprint(raw_data['stop_areas'][0])


# with open('./gares.csv', mode="w") as csvFile:
#     csv_reader = csv.DictReader(csvFile)
#     csv_writer = csv.writer(csvFile, delimiter=' ')

#     for i in range(len(raw_data['stop_areas'])):
#         if(raw_data['stop_areas'][i]['label'] != ''):
#             if(raw_data['stop_areas'][i]['label'] != '.'):
#                 label = raw_data['stop_areas'][i]['label']
#                 codes = raw_data['stop_areas'][i]['codes']
#                 coord = raw_data['stop_areas'][i]['coord']
#                 admin_regions = raw_data['stop_areas'][i]['administrative_regions'][0]
#                 csv_writer.writerow(f" Les informations de la régions administratives sont : {admin_regions}.\n Les codes sont :{codes}.\n  Les coordonnées de la gare sont : {coord}.\n Les labels de la gare sont : {label}.\n ")

# writer.writerow(raw_data['stop_areas'][i]['codes'])
# writer.writerow(raw_data['stop_areas'][i]['label'])
# writer.writerow(raw_data['stop_areas'][i]['coord'])
# writer.writerow(raw_data['stop_areas'][i]['administrative_regions'][0])

# def searchStation(to, from):
#     url = journeysUrl
#     api_key = token_auth
#     destination1 = from
#     destination2 = to
#     json_obj = urllib.urlopen()
#     final_url =  url + "?from" + destination1 + "&to" + destination2

#     for item in raw_data




# # Write to .CSV
# with open('./gares.csv', mode="w") as csvFile:
#     writer = csv.writer(csvFile, delimiter=',')

#     writer.writerow(r)
# for line in codes:
#     writer.writerow(line)


#     for i in range(len(raw_data['stop_areas'])):
#         if(raw_data['stop_areas'][i]['label'] != ''):
#             if(raw_data['stop_areas'][i]['label'] != '.'):
#                 label = raw_data['stop_areas'][i]['label']
#                 codes = raw_data['stop_areas'][i]['codes']
#                 coord = raw_data['stop_areas'][i]['coord']
#                 admin_regions = raw_data['stop_areas'][i]['administrative_regions'][0]


# with open('./gares.csv', mode="w") as csvFile:
#     csv_writer = csv.writer(csvFile, delimiter='')
#     csv_reader = csv.reader()
#         csv_writer.writerow(f" Les informations de la régions administratives sont : {admin_regions}.\n Les codes sont :{codes}.\n  Les coordonnées de la gare sont : {coord}.\n Les labels de la gare sont : {label}.\n ")


