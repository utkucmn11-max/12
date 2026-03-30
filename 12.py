import streamlit as st

# 1. Sayfa konfigürasyonu (Mutlaka en üstte olmalı)
st.set_page_config(
    page_title="Sadece Senin İçin",
    page_icon="❤️",
    layout="centered"
)

# 2. CSS Düzenlemesi (Hatalı kısım düzeltildi)
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .stApp {
        background-image: linear-gradient(135deg, #feb2b2 0%, #feb2b2 100%);
    }
    .love-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1 {
        color: #e53e3e !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True) # Parametreyi unsafe_allow_html olarak düzelttik

# 3. İçerik Alanı
st.markdown('<div class="love-card">', unsafe_allow_html=True)
st.title("İyi Ki Varsın ❤️")
st.write("Senin için küçük bir dijital sürpriz hazırlamak istedim.")
st.markdown('</div>', unsafe_allow_html=True)

st.write("") # Boşluk

if st.button("Seni ne kadar sevdiğimi gör! ✨"):
    st.balloons()
    st.success("Sonsuza kadar! ❤️")

# Sayfa altına küçük bir not
st.markdown("---")
st.caption("2026 | Senin için sevgiyle kodlandı.")
