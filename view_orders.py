import streamlit as st
from config import baseUrl
import requests

def view_orders_page():
    st.title("View Orders")
    get_orders=requests.get(baseUrl+f"/brand/orders/{st.session_state.partner_id}")
    if get_orders.status_code==200:
        print("got data")
        st.dataframe(get_orders.json())
    else:
        st.error(get_orders)