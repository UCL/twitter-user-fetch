from app.twitterfetch import authenticate
import unittest


class TestCredentials(unittest.TestCase):

    def test_get_access_json(self):
        auth = authenticate.Authenticate()
        result = authenticate.Authenticate.get_access_token(auth)
        self.assertRegex(result, "^[A-Za-z0-9%]+")
