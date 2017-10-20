from app.frequency import calculate
import unittest


class TestCalculate(unittest.TestCase):

    dl = [
        ['Tue Sep 19 11:53:24 +0000 2017', '#alltestsmatter1'],
        ['Thu Sep 21 11:53:24 +0000 2017', '#alltestsmatter2'],
        ['Thu Oct 19 11:53:24 +0000 2017', '#alltestsmatter1'],
        ['Thu Oct 19 11:53:24 +0000 2017', '#alltestsmatter1'],
        ['Thu Oct 19 11:53:24 +0000 2017', '#alltestsmatter2'],
        ['Thu Oct 19 11:53:24 +0000 2017', '#alltestsmatter2'],
        ['Thu Oct 19 11:53:24 +0000 2017', '#alltestsmatter2'],
    ]

    def test_get_monthly_frequency(self):
        expected = [
            [2017, 9, '#alltestsmatter1', 1],
            [2017, 9, '#alltestsmatter2', 1],
            [2017, 10, '#alltestsmatter1', 2],
            [2017, 10, '#alltestsmatter2', 3]
        ]
        calc_df = calculate.Calculate(self.dl)
        self.assertListEqual(calc_df.get_monthly_frequency().values.tolist(), expected, "Must calculate frequency")

    def test_get_average_monthly_frequency(self):
        expected = [
            ['#alltestsmatter1', 1.5],
            ['#alltestsmatter2', 2.0]
        ]
        calc_df = calculate.Calculate(self.dl)
        self.assertListEqual(calc_df.get_average_monthly_frequency().values.tolist(), expected, "Must calculate avg")
