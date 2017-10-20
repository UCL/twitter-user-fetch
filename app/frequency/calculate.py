import pandas
from datetime import datetime


class Calculate(object):
    """
    Performs the calculations for monthly frequency and average of monthly frequency. It uses Panda
    https://pandas.pydata.org/pandas-docs/stable/api.html
    """

    date_format = "%a %b %d %H:%M:%S %z %Y"

    def __init__(self, datalist):
        """
        Constructor instantiates a Panda data frame from the list of lists datalist object. It converts the created_at
        field provided by Twitter API into a datetime.
        """
        self.df = pandas.DataFrame(datalist, columns=['date_created', 'stem'])
        self.df['timestamp'] = self.df['date_created'].apply(lambda x: datetime.strptime(x, self.date_format))
        self.df.drop('date_created', axis=1, inplace=True)
        self.df['year'] = self.df['timestamp'].dt.year
        self.df['month'] = self.df['timestamp'].dt.month
        self.df['stem_freq'] = self.df['stem']

    def get_monthly_frequency(self):
        """
        Obtains the monthly frequency for each word stem
        """
        return self.df.groupby(['year', 'month', 'stem'], as_index=False)[['stem_freq']].count()

    def get_average_monthly_frequency(self):
        """
        Obtains the average monthly frequency for each word stem
        """
        return self.get_monthly_frequency().groupby(['stem'], as_index=False)[['stem_freq']].mean()

    def get_average_monthly_frequency_descending(self):
        """
        Sorts the average monthly frequency of stems in descending order
        """
        return self.get_average_monthly_frequency().sort_values(by='stem_freq', ascending=False)
