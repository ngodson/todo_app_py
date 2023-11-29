import streamlit as st
from PIL import Image


with st.expander("start camera"):
    # start camera
    camera_image = st.camera_input("Take a shot")

# if statement is executed to ensure camera permission is successful before code block
if camera_image:
    # create a pillow image
    img = Image.open(camera_image)

    # convert the pillow image to grayscale
    gray_img = img.convert("L")
    # L is an arguement that converts to gray scale

    # render grayscale image on webpage
    st.image(gray_img)