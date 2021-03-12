import streamlit as st
import numpy as np
import pandas as pd

# Sketch 
st.title('your **Quantitative**')

st.markdown('Are you looking for a quick way to skin and scam protfolio holdings of big ETFs, mutual Funds ... ?')
st.markdown('your **Quantitative** is here to help you. Follow these steps:')

# Step 1: Getting categorize input
# TODO: Add categorz of type of asset: small cap, ..... 
st.markdown('1. Give a name to dataset being uploaded.')
provider = {1: "Blackrock", 2: "Vanguard", 3: "Other"}

def format_func(option):
    return provider[option]

option = st.selectbox("Select option", options=list(provider.keys()), format_func=format_func)
st.write(f"You selected option {option} called {format_func(option)}")

# Step 2: Input data
st.markdown('2. Drag&Drop .csv file. You will be able to see the data frame.')

data = st.file_uploader("Upload dataset", type=["csv"])

if data is not None:
    df = pd.read_csv(data)
    st.dataframe(df.head())

    # Step 3: Analyse
    st.markdown('3. Select the analysis that your **Quantitative** is supposed to do for you.')

    manipulate = st.selectbox('Do you want to manipulate the dataframe?', ('Group data by', 'Sort', 'To be defined'))
    st.write('You selected:', manipulate)

    # Step 3.1: Structural manipulations

    # Step 3.1.1 Feature group by desired combination
    if manipulate == 'Group data by':
        list_columns = df.columns.tolist()
        target_columns = st.multiselect("Group columns", list_columns)
    
        desiredGrouping = df[target_columns]

        if len(target_columns) > 0:
            desiredGrouping
        
    if manipulate == 'Sort':
        sortingTypes = ['Weight: max to min', 'Weight: max to min', 'Price: max to min', 'Price: min to max', 'To be defined']
        desiredSorting = st.multiselect("Select sorting type", sortingTypes)
        list_columns = df.columns.tolist()
        target_columns = st.multiselect("Sort columns", list_columns)

        if desiredSorting == 'Weight: max to min':
            sorted_df = df[target_columns].sort_values(ascending=False)
            sorted_df


    





    st.markdown('4. Results will be plotted.')
        







    