# Dependencies from 3rd
import yfinance as yf
import pandas as pd

def chooseAsset(ticker):
    asset = yf.Ticker(ticker)
    return asset

def inform(asset):
    #information = pd.DataFrame(asset.info)
    information = asset.info
    return information



