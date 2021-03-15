# Dependencies
import pandas as pd

# Constructor features 
#
# 1. Count number of different values
def extract_target(dataframe, custom_column, target):
    index = custom_column.index(target)
    series = dataframe.iloc[:, index]
    return series

def count_attribute(series):
    return pd.value_counts(series)