import urllib.request
import json
from app.twitterfetch import credentials


class Authenticate(object):
    """
    Authenticate against Twitter API. Return the access_token obtained from the API
    https://developer.twitter.com/en/docs/basics/authentication/overview/application-only
    """

    twitter_api_auth_url = "https://api.twitter.com/oauth2/token"

    def get_access_token(self, data, headers):
        req = urllib.request.Request(self.twitter_api_auth_url, data, headers)
        resp = urllib.request.urlopen(req).read()
        return json.loads(resp.decode('utf-8'))['access_token']

    def get_headers(self):
        concatenate_credentials = credentials.get_bearer_token_credentials(credentials.Credentials())
        bearer_token = credentials.get_base64_bearer_token_credentials(concatenate_credentials)
        headers = {'Authorization': 'Basic ' + bearer_token,
                   'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        return headers

    def get_request_body(self):
        values = {'grant_type': 'client_credentials'}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        return data
