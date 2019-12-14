import pandas as pd
import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt
import seaborn as sns
import random

class DataGen:

    def new_dataset(self, features: list) -> pd.DataFrame:
        '''
        Datasets are structured as Pandas Dataframes
        A new dataset requires at least one feature
        '''
        df = pd.DataFrame(data=features)
        return df

    def add_feature(self, feature_name, distribution=scs.norm, size=100):
        pass

    def get_features():
        pass

    def hist():
        pass

    def write_data():
        pass


