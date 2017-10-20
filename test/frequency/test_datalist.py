from app.frequency import datalist
import unittest


class TestDataList(unittest.TestCase):

    def test_date_and_stem_datalist(self):
        date_and_stem_df = datalist.DateAndStemDataList()
        date_and_stem_df.append_to_datalist('Thu Oct 19 11:53:24 +0000 2017', ['test', 'tweet', '#alltestsmatter'])
        self.assertListEqual(date_and_stem_df.datalist[2], ['Thu Oct 19 11:53:24 +0000 2017', '#alltestsmatter'])
