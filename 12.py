import streamlit as st

# ÖNEMLİ: Bu komut her zaman en üstte, diğer st. komutlarından önce olmalı!
st.set_page_config(
    page_title="Bizim Hikayemiz", 
    page_icon="❤️", 
    layout="centered" # "wide" yaparak geniş ekran da kullanabilirsin
)

# Arka plan ve yazı tipleri için özel CSS (Daha temiz bir görünüm için)
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stApp {
        background-image: linear-gradient(to bottom, #ff9a9e 0%, #fecfef 100%);
    }
    h1 {
        color: white;
        text-shadow: 2px 2px 4px #00000033;
        text-align: center;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("Seni Sevmemin Binlerce Sebebi Var... ❤️")

# Diğer bölümler buraya gelecek...
