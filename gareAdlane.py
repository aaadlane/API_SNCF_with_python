from os import write
from pprint import pprint
import json
import requests
import csv
import urllib

# https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025

# url = "https://api.sncf.com/v1/coverage/sncf/stop_areas/"
url = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
token_auth = '5467e28e-385b-4f3c-8bbd-8a5c4d9f3b38'
urltest = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&direct_path=none&last_section_mode%5B%5D=walking&is_journey_schedules=True&datetime=20210125T115200&to=stop_area:OCE:SA:87722025&min_nb_journeys=5&min_nb_transfers=0&allowed_id%5B%5D=stop_point:OCE:SP:TGVINOUI-87722025&allowed_id%5B%5D=stop_point:OCE:SP:TGVINOUI-87686006&first_section_mode%5B%5D=walking"
token_password = ''
r = requests.get(urltest, auth=(token_auth, token_password))
raw_data = json.loads(r.text)
text_json = json.dumps(raw_data)

journeysUrl = 'https://api.sncf.com/v1/coverage/sncf/journeys/'
journeys_request = requests.get(journeysUrl, auth=(token_auth, token_password))
journeys_data = json.loads(journeys_request.text)
pprint(r.json())
# pprint(r.json()['journeys'])




for i in r.json()["journeys"]:
    pprint(i)

with open('./test.json', 'w') as outfile:
    json.dump(r.json(), outfile, indent=4)

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


# journeys = "journeys": [{"sections": [{"stop_date_times": [{"stop_point": {"name: 'gare de lyon'}}]}]}]


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
