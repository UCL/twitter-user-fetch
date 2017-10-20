class DateAndStemDataList(object):
    """
    Data container to be used in a data frame in Pandas
    https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe
    """

    def __init__(self):
        """
        Creates a list of lists as a container for data
        """
        self.datalist = []

    def append_to_datalist(self, date, stems):
        """
        Appends a list to datalist in the format [date, stem]
        """
        for stem in stems:
            self.datalist.append([date, stem])
