# Dependencies
import pandas as pd

# 1. Count number of different values
def extract_target(dataframe, custom_column, target):
    index = custom_column.index(target)
    series = dataframe.iloc[:, index]
    return series

def count_attribute(series):
    counts = pd.value_counts(series)
    return counts

# 2. Specify insights
def dive_deeper(counts):
    countList = counts.keys()
    return countList

def get_columns_options(dataframe):
    myColumn = dataframe.columns.tolist()
    return myColumn

def get_column_values(dataframe, column):
    key = dataframe[column].tolist()
    return key
