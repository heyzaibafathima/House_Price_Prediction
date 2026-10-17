
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Home Price Prediction")
st.write("Enter the house details to predict its price.")

# Input fields
area = st.number_input("Area (sq. ft.)", min_value=1, value=3000)
bedrooms = st.number_input("Number of Rooms", min_value=1, value=3)
age = st.number_input("Age of the House (years)", min_value=0, value=40)

if st.button("Predict Price"):
    input_data = pd.DataFrame(
        [[area, bedrooms, age]],
        columns=model.feature_names_in_
    )

    price = model.predict(input_data)

    st.success(f"Predicted House Price: Rs. {price[0]:,.2f}")
