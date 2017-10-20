import unittest
import twitterUserFetch


class TestTwitterUserFetch(unittest.TestCase):

    test_user = "mrguzmanmeuk"

    def test_get_tweets_for_user(self):
        self.assertTrue(len(twitterUserFetch.get_tweets_for_user(self.test_user)) >= 21, "Returns at least 21 tweets")

    def test_get_word_stems(self):
        tw_text = 'Java not dead: When Web Companies Grow Up They Turn Into Java Shops [Video] ' \
                  'https://t.co/P8pi4dZtHN via @DZone #java #web'
        expected = ['java', 'dead', 'web', 'compani', 'grow', 'turn', 'java', 'shop', 'video',
                    'https://t.co/p8pi4dzthn', 'via', '#java', '#web']
        self.assertListEqual(twitterUserFetch.get_word_stems(tw_text), expected)
