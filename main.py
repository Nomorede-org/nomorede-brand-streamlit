from create_catalogue import CreateCatalogue
from create_product import CreateProduct
from profile_1 import profile
import streamlit as st
import json
from config import baseUrl
import requests
from login import login
from create_user import CreateUser
from streamlit_option_menu import option_menu
# Streamlit Page Configuration
st.set_page_config(
    page_title="Nomorede",
    page_icon="asssets/5.ico",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.nomorede.com/contactUs',
        'Report a bug': "https://www.nomorede.com/contactUs",
        'About': "One Stop Science Backed styling aggregator platform"
    }
)


with st.sidebar:
    selected = option_menu("Main Menu", ['Profile',"Login","Create User","Create Catalogue","Create Product"], 
        icons=['bi-person-fill', 'bi-box-arrow-in-right',"bi-person-fill-add",'bi-book-fill',"bi-box-fill"], menu_icon="bi-list", default_index=1)

if selected.lower()=="login":
    st.title("Login")
    st.divider()
    login()

if selected.lower()=='profile':
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        profile()

if selected.lower()=='create user':
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        st.title("Create User")
        CreateUser()

if selected.lower()=="create product":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        st.title("Create Product")
        CreateProduct()

if selected.lower()=="create catalogue":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        CreateCatalogue()