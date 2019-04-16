from django.test import TestCase
from models import *

# Create your tests here.

class  Test(TestCase):

    def test_ttn_mean(self):

        input_data = [
            [9, 9, 9, 9],
            [5, 5, 7, 7],
            [8, 9, 10, 10],
            [3, 4, 4],
            [3, 6, 6, 8],
            [5, 5, 9, 10],
            [8, 8, 8],
            [5, 5, 8, 8, 9],
            [4, 5, 6, 7, 9],
            [10, 10, 10, 10, 10],
            [2, 8, 8, 9, 9, 9],
            [4, 6, 8, 8, 10],
            [7, 8, 8, 8, 8],
            [4, 4, 6, 6, 6, 6],
        ]
        res_data = [
            9.0,
            6.0,
            9.25,
            11/3.,
            5.75,
            7.25,
            8.0,
            7.0,
            24.5/4,
            10.0,
            7.9,
            7.25,
            31.5/4,
            5.4,
        ]
        for inp, res in zip(input_data, res_data):
            self.assertEqual(ttn_mean(inp), res)