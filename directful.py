
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

"""img = Image.open("room_image.jpeg")
st.image(img, caption="room")"""

"""page_bg_img =
<style>
body {
background-image: url("https://static.leonardo-hotels.com/image/leonardohotelbucharestcitycenter_room_comfortdouble2_2022_4000x2600_7e18f254bc75491965d36cc312e8111f_2048x1331_desktop_2.webp");
background-size: cover;
}
</style>

st.markdown(page_bg_img, unsafe_allow_html=True)"""


def set_background(url):
    if url:
        page_bg_img = '''
        <style>
        body {
            background-image: url("''' + url + '''");
            background-size: cover;
        }
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit uygulaması
def main():
    # Arka plan resminin URL'sini belirleyin
    background_url = "https://static.leonardo-hotels.com/image/leonardohotelbucharestcitycenter_room_comfortdouble2_2022_4000x2600_7e18f254bc75491965d36cc312e8111f_2048x1331_desktop_2.webp"
    
    # Arka plan resmini ayarlayın
    set_background(background_url)
    
    # Diğer içeriği ekleyin
    st.title("Streamlit Web Uygulaması")
    st.write("Merhaba, dünyaya hoş geldiniz!")

if __name__ == "__main__":
    main()



