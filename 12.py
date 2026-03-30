import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.let_it_rain import rain # Kalp efekti için

# 1. SAYFA YAPILANDIRMASI (Hata almamak için EN ÜSTTE olmalı)
st.set_page_config(
    page_title="Bizim Dünyamız ❤️",
    page_icon="🌸",
    layout="centered" # İçeriği yatayda ortalar
)

# 2. ÖZEL CSS TASARIMI
st.markdown("""
    <style>
    /* Arka plan rengi (Açık pembe/krem) */
    .stApp {
        background-color: #fff0f3;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Ana başlık stili */
    .stTitle h1 {
        color: #d81b60 !important;
        text-align: center !important;
        font-size: 3rem !important;
        margin-bottom: 0px;
    }

    /* Alt başlık stili */
    .stSubheader h3 {
        color: #555 !important;
        text-align: center !important;
        margin-bottom: 25px;
    }

    /* "Neden Sen?" kart stili */
    .not-kart {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4081;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        color: #333;
    }
    
    /* Yan menü (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #fce4ec;
    }
    [data-testid="stSidebar"] h1 {
        color: #d81b60;
    }
    </style>
    """, unsafe_allow_html=True) # Burası unsafe_allow_html olmalı

# 3. YAN MENÜ (SIDEBAR)
with st.sidebar:
    st.title("💖 Menü")
    sayfa = st.radio("Gitmek istediğin yer:", ["Ana Sayfa", "Bizim Hikayemiz", "Neden Sen?"])
    st.markdown("---")
    st.write("Her anımız, en güzel hatıramız... ✨")

# 4. SAYFA İÇERİKLERİ VE TAM ORTALAMA
if sayfa == "Ana Sayfa":
    st.title("İyi Ki Varsın ❤️")
    st.subheader("Birlikte Geçen Her An Çok Değerli")
    
    # Kendi profil fotoğrafını veya ortak bir fotoğrafı buraya koyabilirsin
    # st.image("resim_yolu.jpg", use_column_width=True) # use_column_width ortalar
    
    # İçeriği dikeyde de tam ortaya almak için boşluk
    st.write("###")
    
    # Tam ortalanmış bir kart içinde giriş metni
    st.markdown("""
    <div class="not-kart" style="text-align: center;">
        "Hayatımın en güzel hikayesi, seninle tanıştığım o gün başladı. 
        Bu dijital köşe sadece bize, bizim anılarımıza özel... ❤️"
    </div>
    """, unsafe_allow_html=True)

    # 5. KALP BALONU EFEKTİ VE BUTON
    st.write("###") # Boşluk
    
    # Butonu ve efekti dikeyde de tam ortalamak için boşluklar
    st.write("---")
    st.write("###")

    # Tam ortalanmış sütunlar oluştur
    # [1, 1, 1] ifadesi, butonun 3 eşit sütundan ortadakine yerleşmesini sağlar
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        # Butona tıklandığında çalışacak fonksiyon
        def trigger_hearts():
            # Kalp emojisi veya kalp balonu emojisi
            rain(
                emoji="💖", # Veya "🎈" kalp balonu efekti için
                font_size=54,
                falling_speed=5,
                animation_length="4s", # 4 saniye sürer
            )
            # st.toast("Kalbim sana ulaştı! ❤️") # Küçük bir bildirim

        # Butonu tasarla ve ortala
        # `stylable_container` ile butonun rengini değiştirebiliriz
        with stylable_container(
            key="heart_button",
            css_styles="""
                button {
                    background-color: #d81b60 !important;
                    color: white !important;
                    border-radius: 20px !important;
                    width: 100%;
                    font-size: 1.2rem;
                }
            """,
        ):
            if st.button("Bana Tıkla! ✨", on_click=trigger_hearts):
                st.write("") # Boşluk (re-render için gerekli)

    st.write("###") # Butonun altına boşluk

elif sayfa == "Bizim Hikayemiz":
    st.title("Zaman Tünelimiz ⏳")
    st.subheader("En Güzel Hatıralarımız")
    
    st.write("📅 **[Tanıştığımız Gün]:** O gün dünya benim için sanki yeniden dönmeye başladı.")
    # st.image("anilar/resim1.jpg", caption="İlk günümüz...")
    st.write("###")
    st.write("💬 **[İlk Mesaj]:** Heyecandan ellerimin titrediği o anı hala hatırlıyorum.")
    # st.image("anilar/resim2.jpg", caption="İlk mesajlaşmamız...")

elif sayfa == "Neden Sen?":
    st.title("Çünkü... ✨")
    st.subheader("Gönlümü Feth Eden Her Detay")
    
    sebepler = [
        "En kötü günümde bile beni güldürebildiğin için.",
        "Gözlerinin içine baktığımda huzuru bulduğum için.",
        "Sadece yanımda olman bile her şeyi güzelleştirdiği için.",
        "Hayallerime ortak olduğun için.",
        "Favori yerim: Senin yanın olduğu için."
    ]
    
    for s in sebepler:
        st.markdown(f'<div class="not-kart">🌟 {s}</div>', unsafe_allow_html=True)

# 6. ALT BİLGİ (Yine tam ortalanmış)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>2026 | Senin için, seninle birlikte kodlandı. ❤️</p>", unsafe_allow_html=True)
