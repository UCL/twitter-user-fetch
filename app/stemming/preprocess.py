import nltk

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

nltk.download("stopwords")


class PreProcess(object):
    """
    Utility methods to pre-process tweet text data
    """

    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}', '’', '-', '‘', '…', '%',
                       '£', '&', '”', '...'])
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True)

    def remove_stopwords_and_punctuation(self, tweet_text):
        """
        Filters stop words and punctuation characters out from a tweet text. It uses NLTK TweetTokenizer configured to
        remove Twitter handles and convert the text content to lower case.
        :param tweet_text:
        :return: a list containing the filtered string tokens
        """
        word_tokens = self.tweet_tokenizer.tokenize(tweet_text)
        return [token for token in word_tokens if token not in self.stop_words]
