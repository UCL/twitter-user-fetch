from app.twitterfetch import authenticate
import urllib.request
import json


class UserTimeline(object):

    resource_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    date_key = "created_at"
    tweet_key = "text"

    def get_access_token(self):
        auth = authenticate.Authenticate()
        return authenticate.Authenticate.get_access_token(auth)

    def get_tweets(self, screen_name):
        headers = {'Authorization': 'Bearer ' + self.get_access_token()}
        url = self.resource_url + '?screen_name=' + screen_name + '&count=3000'
        req = urllib.request.Request(url, None, headers)
        resp = urllib.request.urlopen(req).read()
        user_timeline = json.loads(resp.decode('utf-8'))
        return [{self.date_key: tweet[self.date_key], self.tweet_key: tweet[self.tweet_key]} for tweet in user_timeline]
