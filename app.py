import streamlit as st
import numpy as np
import pandas as pd
import joblib

scaler = joblib.load('scaler.pkl')
# model = joblib.load('model.pkl')
df = pd.read_csv('cleaned_data.csv')  # ✅ cleaned one

st.title("Real Estate Price Prediction App")

st.divider()

# 'bed','bath','house_size','acre_lot','status','city','state','street'
bed = st.number_input("Enter Number of Bedrooms", value=2, step=1)
bath = st.number_input("Enter Number of Bathrooms", value=1, step=1)
size = st.number_input("Enter Size of the House", value=1000, step=50)

city_options = sorted(df['city'].dropna().unique().tolist())
city = st.selectbox("Select City", city_options)