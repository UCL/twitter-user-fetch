from app.stemming import preprocess
import unittest


class TestPreProcess(unittest.TestCase):

    def test_remove_stopwords_and_punctuation(self):
        sample_tweet = "This a test tweet #alltestsmatter @ucl."
        preprocessor = preprocess.PreProcess()
        expected = ['test', 'tweet', '#alltestsmatter']
        result = preprocessor.remove_stopwords_and_punctuation(sample_tweet)
        self.assertListEqual(result, expected, "Must return a list of tokens without Twitter handles or punctuation")
