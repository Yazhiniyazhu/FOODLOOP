import streamlit as st

st.title("🍲 Donate Food")

food = st.text_input("Food Name")

quantity = st.number_input(
    "Quantity",
    min_value=1
)

expiry = st.date_input("Expiry Date")

location = st.text_area("Pickup Address")

if st.button("Donate"):

    st.success("Food Donation Added Successfully!")

    