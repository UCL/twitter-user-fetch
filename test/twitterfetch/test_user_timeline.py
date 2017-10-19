from app.twitterfetch import user_timeline
import unittest


class TestUserTimeline(unittest.TestCase):

    def test_get_tweets_valid_keys(self):
        """
        {'text': "Text content of the Tweet", 'created_at': 'Thu Oct 19 11:53:24 +0000 2017'}
        """
        timeline = user_timeline.UserTimeline()
        last_tweet = timeline.get_tweets("uclnews")[0]
        result = sorted(last_tweet.keys())
        expected = ['created_at', 'text']
        self.assertEqual(result, expected, "")
