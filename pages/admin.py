import streamlit as st

st.title("👨‍💼 Admin Dashboard")

requests = [
    "Rice - NGO A",
    "Biryani - NGO B",
    "Milk - NGO C"
]

selected = st.selectbox(
    "Pending Requests",
    requests
)

volunteer = st.selectbox(
    "Assign Volunteer",
    [
        "Volunteer 1",
        "Volunteer 2",
        "Volunteer 3"
    ]
)

if st.button("Approve"):

    st.success("Volunteer Assigned")

status = st.selectbox(
    "Delivery Status",
    [
        "Pending",
        "Picked Up",
        "Delivered"
    ]
)

if st.button("Update Status"):

    st.success("Status Updated")