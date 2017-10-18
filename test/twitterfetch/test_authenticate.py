from app.twitterfetch import authenticate
import unittest


class TestCredentials(unittest.TestCase):

    def test_get_access_json(self):
        auth = authenticate.Authenticate()
        headers = authenticate.Authenticate.get_headers(auth)
        data = authenticate.Authenticate.get_request_body(auth)
        result = authenticate.Authenticate.get_access_json(auth, data, headers)
        print(result)
