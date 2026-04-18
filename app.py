import streamlit as st

import joblib

model = joblib.load("house_model.pkl")

st.title("House Price Prediction App")

st.write("Enter house details to predict price")

size = st.number_input("Enter House Size (sq ft)")

bedrooms = st.number_input("Enter Number of Bedrooms")

age = st.number_input("Enter House Age (years)")


if st.button("Predict Price"):
    input_data = [[size, bedrooms, age]]
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")