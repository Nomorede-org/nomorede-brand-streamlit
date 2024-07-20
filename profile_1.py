import streamlit as st
import requests
from config import baseUrl

def profile():
    response = requests.get(baseUrl+f"/user/profile/{st.session_state.partner_id}")
    # Parse JSON response
    data = response.json()
    
    # Create Streamlit app
    st.title("User Profile")
    # Display profile picture
    st.image(data["company_logo"], width=100,caption=data['brand_name'])

    # Display important information
    st.header("Basic Information")
    st.write(f"First Name: {data['first_name']}")
    st.write(f"Last Name: {data['last_name']}")
    st.write(f"Email: {data['email']}")
    st.write(f"Language: {data['language']}")

    st.header("Bank Details")
    st.write(f"Account Holder Name: {data['bank_details']['account_holder_name']}")
    st.write(f"Account Number: {data['bank_details']['account_number']}")
    st.write(f"IFSC Code: {data['bank_details']['ifsc_code']}")

    st.header("Brand Information")
    st.write(f"Brand Name: {data['brand_name']}")
    st.write(f"Brand Website:[Link]({data['brand_website']})")
    st.write(f"Description: {data['description']}")
    st.write(f"No. of Catalogue: {len(data['catalogue_id'])}")
    st.write(f"No. of Employees: {len(data['employee'])}")

    st.header("Contact Information")
    st.write(f"Address: {data['contact_info']['address'][0]['street_address']}, {data['contact_info']['address'][0]['city']}, {data['contact_info']['address'][0]['state']}, {data['contact_info']['address'][0]['country']}")
    st.write(f"Mobile Number: {data['contact_info']['mobile_number'][0]['mobile_number']}")

    st.header("Social Media Handles")
    st.write(f"Facebook: [Link]({data['social_media']['facebook']})")
    st.write(f"Twitter: [Link]({data['social_media']['twitter']})")
    st.write(f"Instagram: [Link]({data['social_media']['instagram']})")
    st.write(f"TikTok: [Link]({data['social_media']['tiktok']})")

    st.header("Warehouse Information")
    st.write(f"Address: {data['ware_house'][0]['address']['street_address']}, {data['ware_house'][0]['address']['city']}, {data['ware_house'][0]['address']['state']}, {data['ware_house'][0]['address']['country']}")
    st.write(f"Contact Number: {data['ware_house'][0]['contact_info'][0]['mobile_number']}")
