from app.twitterfetch import authenticate
import urllib.request
import json


class UserTimeline(object):

    resource_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    def get_access_token(self):
        auth = authenticate.Authenticate()
        return authenticate.Authenticate.get_access_token(auth)

    def get_tweets(self, screen_name):
        headers = {'Authorization': 'Bearer ' + self.get_access_token()}
        url = self.resource_url + '?screen_name=' + screen_name + '&count=3000'
        req = urllib.request.Request(url, None, headers)
        resp = urllib.request.urlopen(req).read()
        return json.loads(resp.decode('utf-8'))
