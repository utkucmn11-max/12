import streamlit as st

# 1. AYARLAR (En üstte durmalı)
st.set_page_config(
    page_title="Bizim Sayfamız",
    page_icon="❤️",
    layout="centered"
)

# 2. CSS - TAM ORTALAMA VE GÖRSEL DÜZENLEME
st.markdown("""
    <style>
    /* Arka Plan */
    .stApp {
        background-color: #fffafa;
    }

    /* Tüm içeriği kapsayan ana merkezleyici */
    .main-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    /* Yazı kartı stili */
    .info-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #ffe4e6;
        margin: 20px 0;
        width: 100%;
    }

    h1 {
        color: #ff4b4b !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Butonun rengi ve şekli */
    .stButton button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 50px !important;
        padding: 0.5rem 2rem !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. İÇERİK YAPISI
with st.container():
    st.markdown('<div class="main-wrapper">', unsafe_allow_html=True)
    
    st.title("İyi Ki Varsın ❤️")
    
    st.markdown("""
        <div class="info-card">
            <p style="font-size: 1.2rem; color: #444;">
                "Seni sevmek, hayatın bana sunduğu en güzel hediye. 
                Bu küçük sayfa, sana olan duygularımın dijital bir yansıması olsun istedim."
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 4. SÜTUNLARLA BUTON ORTALAMA (Hatasız Yöntem)
    # [1, 1, 1] yaparak butonu tam ortadaki sütuna hapsediyoruz
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("Kalplerimi Gönder ✨"):
            st.balloons() # Balonlar uçar
            st.snow()     # Kalp niyetine romantik kar efekti
            st.toast("Seni Seviyorum!")

    st.markdown('</div>', unsafe_allow_html=True)

# Alt Bilgi
st.write("---")
st.caption("2026 | Senin için sevgiyle hazırlandı.")
