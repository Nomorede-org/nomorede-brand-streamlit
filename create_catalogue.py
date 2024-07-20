import requests
import streamlit as st
from config import baseUrl
from create_user import getUser

def CreateCatalogue():
    st.subheader("Catalogues:")
    data=getUser(st.session_state.partner_id)['catalogue_id']
    for i in data:
        catalogue_data=requests.get(baseUrl+f"/brand/catalogue/{i}").json()
        st.write(f"Catalogue Name: {catalogue_data['catalogue_name']}")
        st.write(f"Created By: {catalogue_data['created_by']}")
        st.write(f"Catalogue File: [Link]({catalogue_data['catalogue_file']})")
        st.write(f"No. of Products: {len(catalogue_data['product_id'])}")
    st.divider()
    if 'size_chart' not in st.session_state:
        st.session_state['size_chart'] = []
    st.header("Create New Catalogue")
    catalogue_name = st.text_input("Catalogue Name")
    catalogue_file = st.file_uploader("Catalogue File",type=['pdf'])
    with st.form(key='Size Chart'):
        size_chart={
        "size":st.selectbox("Size",('ONE SIZE','XS', 'S', 'M', 'L', 'XL', 'XXL')),
        "chest": st.number_input("Chest"),
        "waist": st.number_input("waist"),
        "hips": st.number_input("hips"),
        "length": st.number_input("length"),
        "sleeve": st.number_input("sleeve"),
        "bust": st.number_input("bust"),
        "neck": st.number_input("neck"),
        "low_hip": st.number_input("lower hip")
        }
        submitted = st.form_submit_button("Add Size")
        if submitted:
            st.session_state['size_chart'].append(size_chart)

    if st.button("Create Catalogue"):
        payload = {
        "brand_id": st.session_state.partner_id,
        "catalogue_name": catalogue_name,
        "size_chart": st.session_state.size_chart,
        "product_id": [],
        "created_by": "string"
        }
        response = requests.post(baseUrl+"/brand/catalogue/create", json=payload)
        if response.status_code == 200:
            st.success("Catalogue created successfully!")
            catalogue_id=response.json()["catalogue_id"]
            files = {
            'file': (catalogue_file.name, catalogue_file, catalogue_file.type)
            }
            data = {
                'catalogue_id': catalogue_id
            }
            ctalogue_post=requests.post(baseUrl+"/brand/catalogue/uploadpdf",files=files, data=data)
            if ctalogue_post.status_code == 200:
                st.success("Catalogue file uploaded successfully!")
                st.session_state.userdata=getUser(st.session_state.partner_id)
            else:
                st.error("Failed to upload catalogue file. Please try again.")
        else:
            st.error("Failed to create catalogue. Please try again.")
