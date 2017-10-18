from app.twitterfetch import credentials
import unittest


class TestCredentials(unittest.TestCase):

    def test_format_bearer_token_credentials(self):
        result = credentials.get_bearer_token_credentials(MockCredentials())
        self.assertRegex(result, "(.+?):(.+?)", "Format of bearer token is invalid")

    def test_base64_bearer_token_credentials(self):
        mock_credentials = MockCredentials()
        result = credentials.get_base64_bearer_token_credentials(mock_credentials.consumer_key + ':'
                                                                 + mock_credentials.consumer_secret)
        self.assertRegex(result, "^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$",
                         "Format of encoded bearer token is invalid")


class MockCredentials(object):

    def __init__(self):
        self.consumer_key = 'a_consumer_key'
        self.consumer_secret = 'a_consumer_secret'
