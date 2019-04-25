import unittest
import pandas as pd
import datamanagement

class TestFUnctions(unittest.TestCase):
    
    def test_import(self):
        data_test = datamanagement.import_data('test_file.json')
        self.assertIsNotNone(data_test)

    def test_str_to_none(self):
        self.assertIsNotNone(datamanagement.str_to_none(2.0))

    def test_str_to_none2(self):
        self.assertEqual(datamanagement.str_to_none(2.1), 2.1)

    def test_data_without_na(self):
        data_test = pd.DataFrame(data={'longitude': [1, 2, 3], 'latitude': [1, 3, None]})
        self.assertEqual(datamanagement.data_without_na(data_test).shape[0], 2)

    def test_data_with_na(self):
        data_test = pd.DataFrame(data={'longitude': [1, 2, 3], 'latitude': [1, 3, None]})
        self.assertEqual(datamanagement.data_with_na(data_test).shape[0], 1)

    def test_replace_with_coordinates(self):
        data_test = pd.DataFrame(data={'longitude': [1, 2, 3], 'latitude': [1, 3, None], 'coordinates': [None, None, {"latitude": -27.479004,"longitude": 153.028853}]})
        data_test['latitude'] = data_test.apply(lambda x: datamanagement.replace_with_coordinates(x, 'latitude'), axis=1) 
        self.assertEqual(data_test.latitude[2], -27.479004)

if __name__ == '__main__':
    unittest.main()
