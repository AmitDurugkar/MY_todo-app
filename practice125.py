import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")
upload_image = st.file_uploader("upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)