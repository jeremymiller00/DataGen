'''
A set of basic tests for the DataGen class

'''
import unittest
from src.DataGen import DataGen
import pandas as pd

class TestDataGen(unittest.TestCase):

    def test_constructor(self):
        dg = DataGen()
        self.assertIsInstance(dg, DataGen)

    def test_new_dataset(self):
        dg = DataGen()
        data = dg.new_dataset(features = [1,2,3,4,5])
        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()

