import streamlit as st
import time

# 1. AYARLAR (Hata almamak için EN ÜSTTE)
st.set_page_config(
    page_title="Canım Sude'm İçin",
    page_icon="❤️",
    layout="centered"
)

# 2. CSS - SÜTUNLARI VE İÇERİĞİ TAM ORTALAMA
st.markdown("""
    <style>
    /* Arka Plan */
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #fed7e2 100%);
    }

    /* Ana Konteyner Ortalama */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* Kart Tasarımı */
    .love-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(216, 27, 96, 0.1);
        border: 1px solid #fbb6ce;
        max-width: 500px;
        margin: 20px auto;
    }

    h1 {
        color: #d81b60 !important;
        font-family: 'Georgia', serif;
    }

    /* Butonun tam ortalanması için */
    .stButton button {
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 10px 30px !important;
        border: none !important;
        transition: 0.3s;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(216, 27, 96, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. İÇERİK (Sütun hatasını önlemek için div içine aldık)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("Canım Sude'm İçin ❤️")

st.markdown("""
    <div class="love-card">
        <p style="font-size: 1.1rem; color: #4a5568;">
            "Sıradan bir günün, seninle tanışınca nasıl bir mucizeye dönüştüğüne şahit oldum. 
            Bu site, bizim küçük dünyamızın kalbi olsun istedim."
        </p>
        <p style="font-weight: bold; color: #d81b60;">İyi ki varsın, iyi ki benimlesin...</p>
    </div>
    """, unsafe_allow_html=True)

# 4. BUTON VE KALP EFEKTİ (Hatasız Ortalama)
# Sütunları yan yana getirmek yerine, tek bir container içinde ortalıyoruz
col1, col2, col3 = st.columns([1, 2, 1]) # Ortadaki sütun butonu tutar

with col2:
    if st.button("Kalplerimi Gönder ✨"):
        st.balloons() # Balonlar uçar
        st.snow() # Kalp niyetine kar taneleri (romantik bir efekt sağlar)
        st.toast("Seni Seviyorum! ❤️")

st.markdown('</div>', unsafe_allow_html=True)

# 5. ALT BİLGİ
st.write("###")
st.markdown("<p style='text-align: center; color: #a0aec0; font-size: 0.8rem;'>Senin için sevgiyle kodlandı. | 2026</p>", unsafe_allow_html=True)
