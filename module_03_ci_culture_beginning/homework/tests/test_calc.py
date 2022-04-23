import unittest

from module_02_linux.homework.hw_3_2 import app

storage = {"20221009": 45745743}


class TestCalc(unittest.TestCase):
    date = list(storage.keys())[0]
    number = str(list(storage.values())[0])
    year = date[0:4]
    month = date[4:6]

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/add/'
        self.calc_year_url = '/calculate/'

    def test_endpoint_add(self):
        number_link = '/' + self.number
        response = self.app.get(self.base_url + self.date + number_link)
        response_text = response.data.decode()
        self.assertTrue(self.date in response_text)
        self.assertTrue(self.number in response_text)

    def test_endpoint_calculate_year(self):
        response = self.app.get(self.calc_year_url + self.year)
        response_text = response.data.decode()
        self.assertTrue(self.year in response_text)

    def test_endpoint_calculate_month(self):
        month_link = '/' + self.month
        response = self.app.get(self.calc_year_url + self.year + month_link)
        response_text = response.data.decode()
        self.assertTrue(self.month in response_text)

    def test_endpoint_add_valid_date(self):
        test_date = '20221414'
        number_link = '/' + self.number
        with self.assertRaises(Exception):
            self.app.get(self.base_url + test_date + number_link)

    def test_empty_storage(self):
        empty_storage = {}
        with self.assertRaises(Exception):
            date = list(empty_storage.keys())[0]
            year = date[0:4]
            self.app.get(self.calc_year_url + year)
