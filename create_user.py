import requests
import streamlit as st
from config import baseUrl
def getUser(id):
    response = requests.get(baseUrl+f"/user/profile/{id}")
    data = response.json()
    return data

def CreateUser():
    st.subheader("Existing Users:")
    data=getUser(st.session_state.partner_id)
    for i in data['employee']:
        personinfo=getUser(i)
        st.write(f"First Name: {personinfo['first_name']}")
        st.write(f"Last Name: {personinfo['last_name']}")
        st.write(f"Email: {personinfo['email']}")
        st.write(f"User Type: {personinfo['user_type']}")

    st.divider()
    first_name=st.text_input("First Name")
    last_name=st.text_input("Last Name")
    email=st.text_input("Email")
    user_type=st.selectbox(
    "User Type?",
    ("brand_manager", "brand_admin"))

    if st.button("Create User"):
        payload = {
        "user_type": user_type,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "brand_id": st.session_state.partner_id,
        "last_login": [],
        "brand_name": data['brand_name'],
        "created_by": data['first_name']
        }
        response = requests.post(baseUrl+"/brand/users/add", json=payload)
        if response.status_code == 200:
            st.success("User created successfully!")
        else:
            st.error("Failed to create user. Please try again.")