from datetime import datetime
from enum import Enum
import streamlit as st
import requests
from config import baseUrl
from create_user import getUser

class StylingProductCategory(str,Enum):
    # Hair Styling
    HAIR_GELS = "Hair Gels"
    HAIR_SPRAYS = "Hair Sprays"
    HAIR_MOUSSE = "Hair Mousse"
    HAIR_TEXTURIZERS = "Hair Texturizers"
    HAIR_BRUSHES = "Hair Brushes"
    HAIR_DRYERS = "Hair Dryers"
    CURLING_IRONS = "Curling Irons"
    STRAIGHTENERS = "Straighteners"
    HAIR_ACCESSORIES = "Hair Accessories"
    # Skincare Styling
    FACIAL_CLEANSERS = "Facial Cleansers"
    TONERS = "Toners"
    MOISTURIZERS = "Moisturizers"
    SERUMS = "Serums"
    FACE_MASKS = "Face Masks"
    EYE_CREAMS = "Eye Creams"
    LIP_CARE = "Lip Care"
    SUNSCREEN = "Sunscreen"
    # Face Styling
    FOUNDATION = "Foundation"
    CONCEALERS = "Concealers"
    PRIMERS = "Primers"
    BLUSHES = "Blushes"
    BRONZERS = "Bronzers"
    HIGHLIGHTERS = "Highlighters"
    MASCARA = "Mascara"
    EYESHADOW = "Eyeshadow"
    EYELINER = "Eyeliner"
    LIPSTICKS = "Lipsticks"
    LIP_GLOSSES = "Lip Glosses"
    LIP_BALMS = "Lip Balms"
    MAKEUP_BRUSHES = "Makeup Brushes"
    MAKEUP_SPONGES = "Makeup Sponges"
    
    # Eyes Styling
    SUNGLASSES = "Sunglasses"
    EYEWEAR = "Eyewear"
    
    # Ears Styling
    EARRINGS = "Earrings"
    EAR_CUFFS = "Ear Cuffs"
    EAR_WRAPS = "Ear Wraps"
    
    # Neck Styling
    NECKLACES = "Necklaces"
    CHAINS = "Chains"
    PENDANTS = "Pendants"
    CHOKERS = "Chokers"
    SCARVES = "Scarves"
    SHAWLS = "Shawls"
    # Hands Styling
    NAIL_POLISHES = "Nail Polishes"
    NAIL_ART = "Nail Art"
    RINGS = "Rings"
    BRACELETS = "Bracelets"
    # Legs and Feet Styling
    CASUAL_SHOES = "Casual Shoes"
    FORMAL_SHOES = "Formal Shoes"
    ATHLETIC_SHOES = "Athletic Shoes"
    SNEAKERS = "Sneakers"
    LOAFERS = "Loafers"
    HEELS = "Heels"
    FLATS = "Flats"
    SANDALS = "Sandals"
    SLIPPERS = "Slippers"
    BOOTS = "Boots"
    # Clothing and Accessories
    TOPS = "Tops"
    BOTTOMS = "Bottoms"
    DRESSES = "Dresses"
    SUITS = "Suits"
    OUTERWEAR = "Outerwear"
    # SHOES = "Shoes"
    BELTS = "Belts"
    HATS = "Hats"
    CAPS = "Caps"
    GLOVES = "Gloves"
    BAGS = "Bags"
    JACKET="jacket"
    TRENCHCOAT="trenchcoat"

def CreateProduct():
    if 'metadata' not in st.session_state:
        st.session_state['metadata']={}
    if 'special_sale' not in st.session_state:
        st.session_state['special_sale']=[]
    catalogue_data=[]
    catagory_data=list(StylingProductCategory)
    
    catalogue_response=requests.get(baseUrl+f"/brand/product/get/{st.session_state.partner_id}")
    if catalogue_response.status_code==200:
        st.dataframe(catalogue_response.json())
    st.divider()    
    for i in st.session_state.userdata['catalogue_id']:
        response=requests.get(baseUrl+f"/brand/catalogue/{i}").json()
        catalogue_data.append({"catalogue_name":response['catalogue_name'],"_id":response['_id']})
    selected_option = st.selectbox("Select the Catalogue", catalogue_data)
    gender=st.selectbox("Gender",["Male","Female","Unisex"])
    sizes=st.multiselect(
    "Avilable sizes",
    ['ONE SIZE','XS', 'S', 'M', 'L', 'XL', 'XXL'])
    mnp=st.text_input("MNP",placeholder="MNP45678ZWD")
    category=st.selectbox("category",catagory_data)
    tags= st.text_input("Enter comma-separated Tags")
    tags_list=[item.strip() for item in tags.split(",")]
    weight=st.number_input("weight (in Kg)",min_value=0.0, format="%.2f")
    quantity=st.number_input("SKU",min_value=0)
    price=st.number_input("Price")
    price_unit=st.selectbox("Select the Price Unit",["INR","USD","EURO"])
    description=st.text_area("Product Description")
    discounts=st.number_input("Discount (in %)",min_value=0)
    st.subheader("Special Sale:")
    with st.form(key='special_sale_form'):
        start_date = st.date_input("Start Date")
        start_time = st.time_input("Start Time")
        end_date = st.date_input("End Date")
        end_time = st.time_input("End Time")
        price_discount = st.number_input("Price", min_value=0.0)
        price_unit_discount = st.selectbox("Price Unit", ["INR","USD","EURO"])
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            start_datetime = datetime.combine(start_date, start_time)
            end_datetime = datetime.combine(end_date, end_time)
            special_sale_data = {
                "start_date": start_datetime.isoformat(),
                "end_date": end_datetime.isoformat(),
                "price": price_discount,
                "price_unit": price_unit_discount
            }
            st.session_state.special_sale.append(special_sale_data)
    st.write(f"no of sale data added: {len(st.session_state.special_sale)}")
    st.subheader("Meta data")
    with st.form(key='metadata_form'):
        texture = st.text_input("Texture", "")
        color = st.text_input("Color", "")
        fabric = st.text_input("Fabric", "")
        material = st.text_input("Material", "")
        metal = st.text_input("Metal", "")
        pattern = st.text_input("Pattern", "")
        style = st.text_input("Style", "")
        sleeves = st.text_input("Sleeves", "")
        neck_line = st.text_input("Neck Line", "")
        season = st.text_input("Season", "")
        tone = st.text_input("Tone", "")
        body_shape = st.text_input("Body Shape", "")
        face_shape = st.text_input("Face Shape", "")

        # Submit button
        submit_button = st.form_submit_button(label='Submit')
    
        if submit_button:
            # Prepare the metadata
            metadata = {
                "texture": texture,
                "color": color,
                "fabric": fabric,
                "material": material,
                "metal": metal,
                "pattern": pattern,
                "style": style,
                "sleeves": sleeves,
                "neck_line": neck_line,
                "season": season,
                "tone": tone,
                "body_shape": body_shape,
                "face_shape": face_shape
            }
            st.session_state.metadata = metadata
    uploaded_files = st.file_uploader("Choose product images or videos", type=["jpg", "jpeg", "png", "mp4", "avi"], accept_multiple_files=True)
    if st.button("Create Product"):
        payload={
        "brand_id": st.session_state.partner_id,
        "gender": gender,
        "catalogue_id":selected_option['_id'],
        "sizes": sizes,
        "mpn": mnp,
        "metadata":st.session_state.metadata,
        "category": category,
        "tags": tags_list,
        "special_sale": st.session_state.special_sale,
        "weight": weight,
        "images": [],
        "quantity": quantity,
        "price": price,
        "price_unit": price_unit,
        "description": description,
        "reviews": [],
        "discounts": discounts,
        "created_by": st.session_state.userdata['first_name']
        }
        # st.json(payload)
        response = requests.post(baseUrl+"/brand/product/create", json=payload)
        if response.status_code == 200:
            st.session_state.userdata=getUser(st.session_state.partner_id)
            st.success("Product created successfully!")
            product_id=response.json()['product_id']
            if product_id and uploaded_files:
                files = []
                for uploaded_file in uploaded_files:
                    files.append(("files", (uploaded_file.name, uploaded_file, uploaded_file.type)))
                response = requests.post(baseUrl+f"/brand/product/upload/{product_id}", files=files)
                if response.status_code == 200:
                    st.success("Product images uploaded successfully!")
            st.session_state.special_sale.clear()
            st.session_state.metadata.clear()
        else:
            st.error("Product creation failed. Please try again.")
            st.session_state.special_sale.clear()