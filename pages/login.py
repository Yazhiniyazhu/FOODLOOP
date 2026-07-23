import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 FoodLoop Login")

option = st.radio("Choose an option", ["Login", "Register"])

if option == "Login":
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful!")

else:
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    role = st.selectbox(
        "Role",
        ["Donor", "NGO", "Volunteer", "Admin"]
    )

    if st.button("Register"):
        st.success("Registration Successful!")