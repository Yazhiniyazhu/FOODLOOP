import streamlit as st

st.title("🏠 Request Food")

food = st.selectbox(
    "Available Food",
    [
        "Rice",
        "Biryani",
        "Vegetables",
        "Bread",
        "Milk"
    ]
)

qty = st.number_input(
    "Required Quantity",
    min_value=1
)

address = st.text_area("Pickup Address")

if st.button("Request Food"):
    st.success("Food Request Submitted!")