import requests
import streamlit as st
# import json
from config import baseUrl
from create_user import getUser


def login():
    with st.form("login_form"):
        email = st.text_input("Email",placeholder="joe@gmail.com")
        password = st.text_input("Password", type="password",placeholder="********")
        submitted = st.form_submit_button("Login")
        if submitted:
                # Create payload for the POST request
            payload = {
                    "email": email,
                    "password": password
            }
            response = requests.post(baseUrl+"/user/login", json=payload)                
            if response.status_code == 200:
                st.success("Logged in successfully!")
                if response.json()['user_type']=='brand':
                    st.session_state.partner_id=response.json()['partner_id']
                    st.session_state.userdata=getUser(st.session_state.partner_id)
            else:
                st.error("Login failed. Please check your credentials.")