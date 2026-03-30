import streamlit as st
import time

# --- 1. SAYFA AYARLARI (BU HER ZAMAN İLK SATIRDA OLMALIDIR) ---
st.set_page_config(
    page_title="Bizim Hikayemiz ❤️",
    page_icon="🌹",
    layout="centered"
)

# --- 2. GÖRSEL ÖZELLEŞTİRME (CSS) ---
st.markdown("""
    <style>
    /* Arka plan gradyanı */
    .stApp {
        background: linear-gradient(to right, #ffafbd, #ffc3a0);
    }
    
    /* Kart yapısı */
    .ask-kart {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #ff4b4b;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Başlık stili */
    .baslik {
        color: #d81b60;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 40px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_index=True)

# --- 3. YAN MENÜ ---
with st.sidebar:
    st.markdown("### ❤️ Özel Menü")
    sayfa = st.radio("Nereye Bakmak İstersin?", ["Ana Sayfa", "Anılarımız", "Neden Sen?", "Sürpriz ✨"])
    st.markdown("---")
    st.write("Sana olan sevgim, her satır kodda gizli.")

# --- 4. SAYFA İÇERİKLERİ ---

if sayfa == "Ana Sayfa":
    st.markdown('<div class="ask-kart"><h1 class="baslik">Hoş Geldin Her Şeyim ❤️</h1>', unsafe_allow_index=True)
    st.write("Bu site, sadece senin gülüşün gibi güzel anları saklamak için yapıldı.")
    st.write("Sol taraftaki menüden dünyamızı keşfedebilirsin.")
    st.markdown('</div>', unsafe_allow_index=True)
    
    # Küçük bir karşılama balonu
    if st.button("Buraya Tıkla"):
        st.balloons()

elif sayfa == "Anılarımız":
    st.markdown('<h1 class="baslik" style="text-align:center;">📸 Hatıralar</h1>', unsafe_allow_index=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📅 **Tanıştığımız Gün**\n\nHayatımın en şanslı günüydü.")
    with col2:
        st.success("🍦 **İlk Randevu**\n\nZamanın durmasını istediğim o an.")
    
    st.warning("✨ *Daha nice güzel anılara beraber yürümek dileğiyle...*")

elif sayfa == "Neden Sen?":
    st.markdown('<h1 class="baslik" style="text-align:center;">Neden Sen? ❤️</h1>', unsafe_allow_index=True)
    
    sebepler = [
        "Dünyadaki en güzel gülüşe sahip olduğun için.",
        "Sadece bakışlarınla bile beni sakinleştirebildiğin için.",
        "Beni her halimle sevdiğin ve desteklediğin için.",
        "Seninle her şeyin çok daha kolay ve güzel olduğu için."
    ]
    
    for s in sebepler:
        st.markdown(f'<div class="ask-kart">🌟 {s}</div>', unsafe_allow_index=True)

elif sayfa == "Sürpriz ✨":
    st.markdown('<h1 class="baslik" style="text-align:center;">Sana Bir Mesaj 💌</h1>', unsafe_allow_index=True)
    
    st.write("Aşağıdaki butona bas ve bekle...")
    
    if st.button("Seni Seviyorum Çünkü..."):
        with st.spinner('Kalbimden geçenler yükleniyor...'):
            time.sleep(2)
        st.balloons()
        st.snow()
        st.markdown("""
            <div style="background-color: white; padding: 30px; border-radius: 50%; border: 2px solid red;">
                <h2 style="color: red; text-align: center;">İYİ Kİ VARSIN! ❤️</h2>
                <p style="text-align: center; color: #555;">Sen benim başıma gelen en güzel şeysin.</p>
            </div>
        """, unsafe_allow_index=True)

# Alt Bilgi
st.markdown("<br><hr><center>Senin için, sevgiyle tasarlandı. ✨</center>", unsafe_allow_index=True)
