'''
A set of basic tests for the DataGen class

'''
import unittest
from src.AssortmentDataGenerator import AssortmentDataGenerator
import pandas as pd

class TestDataGen(unittest.TestCase):

    def test_constructor(self):
        data = [(1,2,3),[4,5,6]]
        names = ["one", "two", "three"]
        dg = AssortmentDataGenerator(features_data=data, feature_names=names)
        self.assertIsInstance(dg, AssortmentDataGenerator)

#    def test_new_dataset(self):
#        dg = DataGen()
#        data = dg.new_dataset(features = [1,2,3,4,5])
#        self.assertIsInstance(data, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()

