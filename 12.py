import streamlit as st
from streamlit_extras.let_it_rain import rain

# 1. AYARLAR (En üstte durmalı)
st.set_page_config(
    page_title="Sadece Bizim İçin",
    page_icon="❤️",
    layout="centered"
)

# 2. CSS - GÖRSEL DÜZENLEME VE ORTALAMA
st.markdown("""
    <style>
    /* Arka Plan */
    .stApp {
        background-color: #fffafb;
    }

    /* Ana Başlık */
    .stTitle h1 {
        color: #ff4b4b !important;
        text-align: center !important;
        font-family: 'Georgia', serif;
        font-size: 3rem !important;
    }

    /* Kart Tasarımı */
    .love-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(255, 75, 75, 0.1);
        border: 1px solid #ffe4e6;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Butonun Tam Ortalanması */
    div.stButton {
        display: flex;
        justify-content: center;
    }

    .stButton button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 15px 40px !important;
        font-size: 1.2rem !important;
        border: none !important;
        transition: 0.3s;
    }
    
    .stButton button:hover {
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. İÇERİK
st.title("İyi Ki Varsın ❤️")

st.markdown("""
    <div class="love-card">
        <p style="font-size: 1.3rem; color: #444;">
            "Seni sevmek, hayatın bana sunduğu en güzel hediye. 
            Bu küçük sayfa, sana olan duygularımın dijital bir yansıması..."
        </p>
    </div>
    """, unsafe_allow_html=True)

# 4. KALP YAĞMURU FONKSİYONU
def kalpleri_yagdir():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=4,
        animation_length="5s", # 5 saniye boyunca yağar
    )

# 5. TAM ORTALANMIŞ BUTON
# Sütun hatasını önlemek için doğrudan CSS ile ortaladık
if st.button("Sana Olan Sevgimi Gör ✨"):
    kalpleri_yagdir()
    st.toast("Kalplerim sana ulaştı! ❤️")

# Alt Bilgi
st.markdown("<br><br><hr><p style='text-align: center; color: #999;'>2026 | Senin için sevgiyle kodlandı.</p>", unsafe_allow_html=True)
