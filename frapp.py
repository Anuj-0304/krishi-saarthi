import streamlit as st
import pandas as pd
import numpy as np
import base64
from PIL import Image


img = Image.open("website_logo.jpg")
st.image(img,width=200)
#Background color yaha hai..
st.markdown(
    """
    <style>
    .stApp {
        background-color: #dedbd2;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#page wide ans concise yaha hai..
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    /* Global text color */
    html, body, [class*="css"] {
        color: #0a0908 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #0a0908 !important;
    }

    /* Paragraphs, labels, widgets */
    p, span, label, div {
        color: #0a0908 !important;
    }

    /* Streamlit inputs text */
    input, textarea {
        color: #0a0908 !important;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: #0a0908 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#title css change..
st.markdown(
    "<h1 style='text-align: center; color: #0a0908; font-size: 80px;'>Krishi Saarthi</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
    
#government scheme panels..


st.set_page_config(layout="wide")

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

images_with_links = [
    ("img1.jpg","https://pmkisan.gov.in/"),
    ("img2.jpg","https://pmfby.gov.in/"),
    ("img3.jpg","https://pmksy.gov.in/"),
]

html = "<div class='horizontal-scroll'>"

for img, link in images_with_links:
    html += (
        f'<a href="{link}" target="_blank" class="img-link">'
        f'<img src="data:image/jpeg;base64,{img_to_base64(img)}">'
        f'</a>'
    )

html += "</div>"

st.markdown(
    f"""
    <style>
    .horizontal-scroll {{
        display: flex;
        overflow-x: auto;
        gap: 16px;
        padding: 10px;
    }}

    .img-link {{
        flex-shrink: 0;
    }}

    .horizontal-scroll img {{
        width: 700px;
        height: 250px;
        object-fit: cover;
        border-radius: 12px;
        cursor: pointer;
    }}
    </style>
    {html}
    """,
    unsafe_allow_html=True
)
st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
#abhi columns me variaations hai..
cols1, cols2 = st.columns(2)
with cols1:
    with st.expander("Know More About Weather Prediction"):
        st.write("""
        Weather Prediction is a crucial aspect of modern agriculture, enabling farmers to make informed decisions based on anticipated weather conditions. By utilizing advanced meteorological models and data analysis techniques, weather prediction systems can provide accurate forecasts for temperature, rainfall, humidity, and other climatic factors that directly impact crop growth and yield.
        """)

    
    
    APP_URL = "https://weather-prediction-bu7p6nawxu45huhizjyedx.streamlit.app/"

    st.markdown(f"""
    <style>
    .click-card {{
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #e0f2fe, #f8fafc);
        box-shadow: 0 10px 24px rgba(0,0,0,0.12);
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        color: #0a0908;
        transition: 
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background 0.25s ease;
    }}

    .click-card:hover {{
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
        background: linear-gradient(135deg, #d9ed92, #ff9b54);
    }}
    </style>

    <a href="{APP_URL}" target="_blank" style="text-decoration:none">
        <div class="click-card">
            Crop-Disease Detection
        </div>
    </a>

    """, unsafe_allow_html=True)
    st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)
    
############################# 
    
    
with cols2:
    with st.expander("Know More About Crop-Disease Detection"):
        st.write("""
        Crop-Disease Detection is an advanced application that leverages machine learning and image processing techniques to identify diseases in various crops. By analyzing images of plant leaves, the system can accurately diagnose common diseases affecting crops such as tomatoes, potatoes, wheat, and more.
        """)

    
    
    APP_URL = "https://crop-disease-detection-r4kvmjzyew58ewgktelgxh.streamlit.app/"

    st.markdown(f"""
    <style>
    .click-card {{
        padding: 30px;
        border-radius: 18px;
        background: linear-gradient(135deg, #e0f2fe, #f8fafc);
        box-shadow: 0 10px 24px rgba(0,0,0,0.12);
        text-align: center;
        font-size: 22px;
        font-weight: 800;
        color: #0a0908;
        transition: 
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background 0.25s ease;
    }}

    .click-card:hover {{
        transform: translateY(-6px) scale(1.02);
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
        background: linear-gradient(135deg, #d9ed92, #ff9b54);
    }}
    </style>

    <a href="{APP_URL}" target="_blank" style="text-decoration:none">
        <div class="click-card">
            Crop-Disease Detection
        </div>
    </a>

    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: none; height: 3px; background-color: #2c6e49; margin: 20px 0;'>",unsafe_allow_html=True)

#############################
st.markdown(
    "<h1 style='text-align: center; color: #0a0908; font-size: 40px;'>Crop Care/Maintenance advisory</h1>",
    unsafe_allow_html=True
)

    


