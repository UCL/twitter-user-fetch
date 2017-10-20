from nltk.stem import porter, snowball


class WordStem(object):
    """
    Stemming methods as provided by NLTK library
    http://www.nltk.org/howto/stem.html
    """

    def get_porter_stem(self, word):
        """
        Returns the word stem using Porter stemming
        """
        stemmer = porter.PorterStemmer()
        return stemmer.stem(word)

    def get_snowball_stem(self, word):
        """
        Returns the word stem using Snowball stemming
        http://snowball.tartarus.org/algorithms/porter/stemmer.html
        """
        stemmer = snowball.SnowballStemmer("english")
        return stemmer.stem(word)
