
import streamlit as st

# 1. Sayfa Ayarları (Hata almamak için en üstte)
st.set_page_config(
    page_title="Sadece Senin İçin",
    page_icon="🤍",
    layout="centered"
)

# 2. Minimalist Stil (CSS)
st.markdown("""
    <style>
    /* Arka planı tamamen sade ve temiz yapalım */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Yazı fontu ve yerleşimi */
    .mektup-metni {
        font-family: 'Times New Roman', serif;
        color: #2c3e50;
        line-height: 2;
        text-align: center;
        padding: 50px 20px;
    }

    .vurgu {
        color: #e63946;
        font-weight: bold;
        font-style: italic;
    }

    /* Gereksiz Streamlit elementlerini gizle (Opsiyonel - Daha temiz görünüm) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_index=True)

# 3. İçerik (Mektup Kısmı)
st.markdown(f"""
    <div class="mektup-metni">
        <h1 style="font-weight: 200; font-size: 2.5rem; margin-bottom: 50px;">
            İyi ki Varsın...
        </h1>
        
        <p>Bazen kelimelerin yetmediği anlar olur, sadece susup hissetmek istersin.</p>
        
        <p>Seninle geçen her dakika, hayatımın en <span class="vurgu">huzurlu</span> hikayesi gibi.</p>
        
        <p>Gülüşün, en karanlık günlerimde bile yolumu aydınlatan tek ışık.</p>
        
        <p>Bu hayatta verdiğim en doğru kararsın.</p>
        
        <p style="margin-top: 50px; font-size: 0.9rem; letter-spacing: 2px;">
            HER ZAMAN SENİNLE.
        </p>
        
        <div style="font-size: 2rem; margin-top: 30px;">🤍</div>
    </div>
    """, unsafe_allow_index=True)

# 4. Küçük bir efekt (Sayfa yüklendiğinde hafifçe kar yağışı)
st.snow()
