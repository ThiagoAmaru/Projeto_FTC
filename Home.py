import streamlit as st
from PIL import Image as img


st.header("Fome Zero")

st.set_page_config(

    page_title = "Home"
)

image = img.open('image/img_1.jpg')

st.sidebar.markdown("Fome Zero")

st.sidebar.markdown(""""___""")

st.markdown("Como acompanhar esse dashboard?")