import numpy as np 
import pandas as pd
import streamlit as st
import sklearn
import joblib

obj=joblib.load('California_parct.joblib')
model=obj['model']
columns=obj['columns']

st.title('California Housing Price Prediction')
In=[]
for i in columns:
    v=st.number_input(f'Enter {i} , value= ')
    In.append(v)
if st.button('predict'):
    out=model.predict([In])
    st.success(f'The predicted price of the house is : {out}') 
    