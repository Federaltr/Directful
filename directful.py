
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


def set_background(url):
    if url:
        page_bg_img = '''
        <style>
        body {
            background-image: url("''' + "http://melisotel.com.tr/wp-content/uploads/2017/06/B04A6353.jpg" + '''");
            background-size: cover;
        }
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit uygulaması
def main():
    # Arka plan resminin URL'sini belirleyin
    background_url = "http://melisotel.com.tr/wp-content/uploads/2017/06/B04A6353.jpg"
    
    # Arka plan resmini ayarlayın
    set_background(background_url)
    
    # Diğer içeriği ekleyin
    st.title("Streamlit Web Uygulaması")
    st.write("Merhaba, dünyaya hoş geldiniz!")

if __name__ == "__main__":
    main()



