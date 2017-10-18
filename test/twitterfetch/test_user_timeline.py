from app.twitterfetch import user_timeline
import unittest


class TestUserTimeline(unittest.TestCase):

    def test_get_tweets(self):
        timeline = user_timeline.UserTimeline()
        print(timeline.get_tweets("uclnews"))
