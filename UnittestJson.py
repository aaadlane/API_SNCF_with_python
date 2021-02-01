import unittest
import os.path
from os import path
# from gareMouny2 import *
from GareMounyV3 import *


class TestStringMethodsOnClasses(unittest.TestCase):
    
    

    def test_file_json_exists(self):
        self.assertTrue(os.path.isfile('stop_areas.json'))

    def test_file_csv_exists(self):
        self.assertTrue(os.path.exists('stop_areas.csv'))

    def test_get_data_from_json(self):
        api_sncf = ApiSncf()
        self.assertEqual(api_sncf.request_api_sncf, None)

    def test_get_header_columns(self):
        api_sncf = ApiSncf()
        self.assertIs(type(api_sncf.list_header_columns), list)

    def test_get_all_areas(self):
        api_sncf = ApiSncf()
        self.assertIs(type(api_sncf.list_gares), list)

    def status_code(self):
        api_sncf = ApiSncf()
        res = requests.get(api_sncf.url_api, auth=(api_sncf.token_auth,'')) 
        self.assertEquals(res.status, 200)
    
    
if __name__ == '__main__':
        unittest.main(verbosity=2)





# #test sur le fichier fonction  garemouny 2 
# class TestStringMethods(unittest.TestCase):

#     def test_json(self):
#         read_json(url_api)
#         self.assertTrue(os.path.isfile('stop_areas.json'))

#     def test_csv(self):
#         create_csv(list_gares)
#         self.assertTrue(os.path.isfile('stop_areas.csv'))

#     def test_get_data_from_json(self):
#         self.assertIs(type(get_data_from_json()), dict)

#     def test_get_header_columns(self):
#         self.assertIs(type(get_header_columns(list_gares)), list)

#     def test_get_all_areas(self):
#         self.assertIs(type(get_all_areas(list_gares)), list)

# if __name__ == '__main__':
#     unittest.main()

