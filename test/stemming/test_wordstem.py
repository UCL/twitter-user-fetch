from app.stemming import wordstem
import unittest


class TestWordStem(unittest.TestCase):

    def test_get_porter_stem(self):
        word_stemmer = wordstem.WordStem()
        self.assertEqual(word_stemmer.get_porter_stem("finalise"), "finalis", "Porter does not recognise UK spelling")
        self.assertEqual(word_stemmer.get_porter_stem("finalize"), "final", "Porter only recognises US spelling")

    def test_get_snowball_stem(self):
        word_stemmer = wordstem.WordStem()
        self.assertEqual(word_stemmer.get_snowball_stem("finalise"), "finalis", "Snowball doesn't read UK spelling")
        self.assertEqual(word_stemmer.get_snowball_stem("finalize"), "final", "Snowball only recognises US spelling")
