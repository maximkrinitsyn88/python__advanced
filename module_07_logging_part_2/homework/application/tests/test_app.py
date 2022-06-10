import unittest
from ..app_server import app


class TestPostServer(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/server_logs'

    def test_post_log(self):
        data = 'filename = lalalalaa &levelname = blablablablabla &name = `uuuuuuuuuuuuuuu`'
        request = self.app.post(self.base_url, data=str(data))
        self.assertTrue(request.status_code == 200)
