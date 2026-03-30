import streamlit as st
# 3. satırda hata almamak için kütüphanenin yüklü olduğundan emin olmalısın
try:
    from streamlit_extras.let_it_rain import rain
except ImportError:
    st.error("Lütfen terminale 'pip install streamlit-extras' yazarak gerekli paketi yükleyin.")

# 1. AYARLAR
st.set_page_config(
    page_title="Bizim Sayfamız",
    page_icon="❤️",
    layout="centered"
)

# 2. CSS - TAM ORTALAMA
st.markdown("""
    <style>
    .stApp { background-color: #fffafb; }
    .main-text {
        text-align: center;
        color: #ff4b4b;
        font-family: 'Georgia', serif;
    }
    .love-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    /* Butonu ortalamak için */
    div.stButton { display: flex; justify-content: center; }
    .stButton button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 10px 40px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. İÇERİK
st.markdown('<h1 class="main-text">İyi Ki Varsın ❤️</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="love-card">
        <p style="font-size: 1.2rem; color: #444;">
            "Hayatımın en güzel hikayesi seninle başladı. <br> 
            Bu sayfa, sana olan duygularımın küçük bir kanıtı olsun."
        </p>
    </div>
    """, unsafe_allow_html=True)

# 4. KALP YAĞMURU BUTONU
if st.button("Kalplerimi Gönder ✨"):
    # Kalp emojisi ile yağmur efekti
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=3,
        animation_length="5s",
    )
    st.toast("Kalpler yola çıktı! ❤️")

st.markdown("<br><hr><p style='text-align: center; color: #999;'>2026 | Senin için sevgiyle hazırlandı.</p>", unsafe_allow_html=True)
