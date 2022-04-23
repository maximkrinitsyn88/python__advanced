import unittest

from module_04_flask.hw.hw_1_2 import app


class TestRegistration(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration_hw'

    def test_full_reg(self):
        data = {'email': 'qwer@mail.ru',
                'phone': 1234567890,
                'name': 'Ваня',
                'address': 'Биробиджан',
                'index': 24124}
        request = self.app.post(self.base_url, data=data)
        self.assertTrue(request.status_code == 200)

    def test_wrong_email(self):
        data = {'email': 'skughysdijkghsdkoljhlk;sdhjlksdfhj',
                'phone': 1234567890,
                'name': 'Ваня',
                'address': 'Биробиджан',
                'index': 24124}
        request = self.app.post(self.base_url, data=data)
        self.assertTrue(request.status_code == 400)

    def test_wrong_phone(self):
        data = {'email': 'qwer@mail.ru',
                'phone': 123456781254190457457457457457,
                'name': 'Ваня',
                'address': 'Биробиджан',
                'index': 24124}
        request = self.app.post(self.base_url, data=data)
        self.assertTrue(request.status_code == 400)

    def test_wrong_name(self):
        data = {'email': 'qwer@mail.ru',
                'phone': 1234567812,
                'name': '',
                'address': 'Биробиджан',
                'index': 24124}
        request = self.app.post(self.base_url, data=data)
        self.assertTrue(request.status_code == 400)

    def test_wrong_address(self):
        data = {'email': 'qwer@mail.ru',
                'phone': 1234567890,
                'name': 'Ваня',
                'address': '',
                'index': 24124}
        request = self.app.post(self.base_url, data=data)
        self.assertTrue(request.status_code == 400)
