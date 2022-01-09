#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime
import pickle
import streamlit as st
import yfinance as yf


# In[ ]:


pickle_in = open("model_arima.pkl", 'rb') 
model_arima = pickle.load(pickle_in)

#pickle_in = open("model_arima.pkl", 'rb') 
#classifier = pickle.load(pickle_in)

st.title("Gold Price Prediction")
text_input = st.slider('Enter the number of days to forecast the price 0-30', min_value=1 , max_value=30, step=1)
st.button("Prediction of gold price")

predict = model_arima.forecast(steps=text_input)[0]
#model_arima.plot_predict(1,1043)
st.write(predict)
#st.button("Forecast the price")

#tickerSymbol = 'GOOGL'
#tickerData = yf.Ticker('tickersymbol')
#tickerDf = tickerData.history(period ='1d', starts = '2018-1-1', end = '2022-1-8')
#st.line_chart(tickerDf.Close)
#st.line_chart(tickerDf.Volume)

