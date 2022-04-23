import datetime
import unittest

from module_03_ci_culture_beginning.materials.previous_hw_test.hello_word_with_day import app

day_to_word_map = {
    0: "Хорошего понедельника",
    1: "Хорошего вторника",
    2: "Хорошей среды",
    3: "Хорошего четверга",
    4: "Хорошей пятницы",
    5: "Хорошей суббота",
    6: "Хорошего воскресенья",
}


class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_username_with_weekdate(self):
        username = 'username'
        weekday = datetime.datetime.today().weekday()
        today = day_to_word_map[weekday]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(today in response_text)
        self.assertTrue(username in response_text)
