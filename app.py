import streamlit as st

st.set_page_config(
    page_title="FoodLoop",
    page_icon="🍱",
    layout="wide"
)

st.title("🍱 FOODLOOP")

st.subheader("Connecting Surplus Food with People in Need")

st.write("""
Welcome to FoodLoop.

Choose a module from the left sidebar.

✔ Registration & Login

✔ Donate Food

✔ Request Food

✔ Manage Pickup & Delivery
""")

st.image("https://images.unsplash.com/photo-1488521787991-ed7bbaae773c", use_container_width=True)