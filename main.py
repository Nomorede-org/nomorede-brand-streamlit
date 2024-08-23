from create_catalogue import CreateCatalogue
from create_product import CreateProduct
from profile_1 import profile
import streamlit as st
import json
from config import baseUrl
import requests
from login import login
from create_user import CreateUser
from view_orders import view_orders_page

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


# with st.sidebar:
    # selected = option_menu("Main Menu", ['Profile',"Login","Create User","Create Catalogue","Create Product"], 
    #     icons=['bi-person-fill', 'bi-box-arrow-in-right',"bi-person-fill-add",'bi-book-fill',"bi-box-fill"], menu_icon="bi-list", default_index=1)
add_sidebar = st.sidebar.selectbox('Menu', ('Profile',"Login","Create User","Create Catalogue","Create Product","View Orders"),index=1)
if add_sidebar.lower()=="login":
    st.title("Login")
    st.divider()
    login()

if add_sidebar.lower()=='profile':
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        profile()

if add_sidebar.lower()=='create user':
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        st.title("Create User")
        CreateUser()

if add_sidebar.lower()=="create product":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        st.title("Create Product")
        CreateProduct()

if add_sidebar.lower()=="create catalogue":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        CreateCatalogue()

if add_sidebar.lower()=="view orders":
    if 'partner_id' not in st.session_state:
        st.warning("Please login first")
    else:
        view_orders_page()