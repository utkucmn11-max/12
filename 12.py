import streamlit as st
import time

# --- 1. SAYFA AYARLARI (EN ÜSTTE OLMALI) ---
st.set_page_config(
    page_title="Bizim Hikayemiz",
    page_icon="❤️",
    layout="centered"
)

# --- 2. ÖZEL CSS (Görseli Güzelleştirir) ---
st.markdown("""
    <style>
    /* Gradyan Arka Plan */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
    }
    
    /* Başlık Stilini Özelleştirme */
    h1 {
        color: #d81b60 !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        padding-top: 20px;
    }
    
    /* Kart Görünümü */
    .memory-card {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #f48fb1;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Buton Stilini Değiştirme */
    div.stButton > button:first-child {
        background-color: #d81b60;
        color: white;
        border-radius: 20px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_index=True)

# --- 3. ANA İÇERİK ---
st.title("İyi Ki Varsın... ✨")

# Yan menü (Sidebar) üzerinden navigasyon
menu = st.sidebar.radio("Sayfalar", ["Giriş", "Anılarımız", "Neden Sen?", "Geri Sayım"])

if menu == "Giriş":
    st.markdown('<div class="memory-card">', unsafe_allow_index=True)
    st.subheader("Hoş Geldin Hayatım")
    st.write("Bu site, sadece senin için ve bizim için tasarlandı. Sol taraftaki menüden dünyamıza göz atabilirsin.")
    st.markdown('</div>', unsafe_allow_index=True)
    
    # Küçük bir animasyonlu buton
    if st.button("Seni ne kadar sevdiğimi görmek için tıkla!"):
        st.balloons()
        st.success("Sonsuza kadar! ❤️")

elif menu == "Anılarımız":
    st.subheader("📸 Unutulmaz Anlar")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://via.placeholder.com/300", caption="İlk günümüz...")
    with col2:
        st.image("https://via.placeholder.com/300", caption="En sevdiğim gülüşün.")

elif menu == "Neden Sen?":
    st.subheader("💌 Benim İçin Anlamın")
    sebepler = [
        "Gülüşünle dünyamı aydınlattığın için,",
        "Her zaman yanımda olduğunu hissettirdiğin için,",
        "En küçük detayları bile unutmadığın için,",
        "Sadece 'sen' olduğun için."
    ]
    for sebep in sebepler:
        st.info(sebep)

elif menu == "Geri Sayım":
    st.subheader("⏳ Geleceğe Doğru")
    # Örnek: Yıldönümü veya buluşma tarihi
    hedef_tarih = "Seni Tanıdığım İlk An"
    st.metric(label="Birlikte Geçen Günler", value="365+", delta="Ve saymaya devam ediyoruz!")

# --- 4. ALT BİLGİ ---
st.markdown("---")
st.caption("Senin için sevgiyle kodlandı. ❤️")
