# Dependencies from 3rd
# [TODO]: Organize dependencies and each respective files
import streamlit as st
import pandas as pd

# Dependencies from me
import constructor as builder
import quantitative as quant

# Sketch 
st.title('your **Quant**')
st.markdown('### @theConstructor')
st.markdown('> Are you looking for a quick way to skin and scam protfolio holdings of big ETFs, mutual Funds, private Funds, or any other asset data frame? If yes, your **Quantitative** is here to help you. Follow these steps: ')

# Step 1: Getting categorize input
# [TODO]: Add category of type of portfolio: small cap, ..... & category date: a.k.a last time data was updated.
st.markdown('**1. Please categorize the data being uploaded.**')
category = st.text_input('Please, categorize the data you will be uploading.', 'Invesco S&P 500 High Dividend Low Volatility ETF (SPHD)')
date = st.date_input('Data is as recent as:')
name = st.write('The data is:', category, date)

if category != "" and date != "":
    # Step 2: Input data
    st.markdown('**2. Drag&Drop .csv file. You will be able to see the data frame and its dimensions.**')
    data = st.file_uploader('Upload dataset', type=['csv'])

    if data is not None:
        df = pd.read_csv(data)
        st.dataframe(df.head())

        totalAssets = len(df)
        totalAttributes = len(df.columns)

        st.markdown('**Total assets:**')
        totalAssets

        st.markdown('**Total attributes:**')
        totalAttributes
        
        # Constructor features start here
        # Step 3: Analyse
        st.markdown('**3. Select the analysis that your Quant is supposed to do for you.**')

        manipulate = st.selectbox('How do you want to manipulate the dataframe?', ('Group data by', 'other...'))
        st.write('You selected:', manipulate)

        # Step 3.1: Structural manipulations
        # Step 3.1.1 Feature group by desired combination
        if manipulate == 'Group data by':
            list_columns = df.columns.tolist()
            target_columns = st.multiselect('Group columns', list_columns)
        
            desiredGrouping = df[target_columns]

            if len(target_columns) > 0:
                desiredGrouping
                customColumns = desiredGrouping.columns.tolist()

                # Feature B1: Constructor.py
                target = st.selectbox('Feel free to select any desired column to count the diffent values that each contain.', customColumns)   
                countInsight = builder.count_attribute(builder.extract_target(desiredGrouping, customColumns, target))
                countInsight

                st.bar_chart(countInsight)

                # Feature B2: Constructor.py
                goDeep = st.selectbox('Want to go deeper in:', builder.dive_deeper(countInsight))
                newDataframe = df.loc[df[target] == goDeep]
                newDataframe

                # Feature B2 & Q1: QUANT API IMPORT
                target_option = st.selectbox('Select column you want to retrieve data from:', builder.get_columns_options(newDataframe))
                company = st.selectbox('Specify company:', builder.get_column_values(newDataframe, target_option))        
                ticker = quant.chooseAsset(company)
                get = quant.inform(ticker)
                get


        







    