import streamlit as st
import time

# 1. SAYFA AYARLARI (Hata almamak için her zaman en üstte!)
st.set_page_config(
    page_title="Bizim Dünyamız ❤️",
    page_icon="🌸",
    layout="centered"
)

# 2. ÖZEL TASARIM (CSS)
st.markdown("""
    <style>
    /* Arka plan rengi ve genel font */
    .stApp {
        background-color: #fffafb;
    }
    
    /* Başlık stili */
    .ana-baslik {
        font-family: 'Georgia', serif;
        color: #c2185b;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Kart tasarımı */
    .not-kart {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4081;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    /* Yan menü (Sidebar) */
    [data-testid="stSidebar"] {
        background-color: #fce4ec;
    }
    </style>
    """, unsafe_allow_index=True)

# 3. YAN MENÜ NAVİGASYON
with st.sidebar:
    st.title("💖 Menü")
    sayfa = st.radio("Gitmek istediğin yer:", ["Giriş", "Bizim Hikayemiz", "Neden Sen?", "Küçük Bir Sürpriz"])
    st.markdown("---")
    st.write("Her anımız, en güzel hatıramız... ✨")

# 4. SAYFA İÇERİKLERİ
if sayfa == "Giriş":
    st.markdown('<h1 class="ana-baslik">Hoş Geldin Her Şeyim... ❤️</h1>', unsafe_allow_index=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Buraya kendi profil fotoğrafını veya ortak bir fotoğrafı koyabilirsin
        st.image("https://cdn-icons-png.flaticon.com/512/4359/4359295.png", width=200)
    
    st.markdown("""
    <div class="not-kart">
        <p style="text-align: center; font-size: 1.2rem; color: #555;">
            "Sıradan bir günün, seninle tanışınca nasıl bir mucizeye dönüştüğünü unutamam. 
            Bu site, bizim küçük dünyamızın dijital bir arşivi olsun istedim."
        </p>
    </div>
    """, unsafe_allow_index=True)

elif sayfa == "Bizim Hikayemiz":
    st.markdown('<h1 class="ana-baslik">Zaman Tünelimiz ⏳</h1>', unsafe_allow_index=True)
    
    # Anılar listesi
    anilar = [
        ("📅 İlk Karşılaşma", "O gün dünya benim için sanki yeniden dönmeye başladı."),
        ("💬 İlk Mesaj", "Heyecandan ellerimin titrediği o anı hala hatırlıyorum."),
        ("🍦 İlk Buluşma", "En sevdiğimiz o yerde, saatlerce hiç susmadan konuşmuştuk.")
    ]
    
    for baslik, detay in anilar:
        with st.expander(baslik):
            st.write(detay)
            # st.image("anilar/resim1.jpg") # Kendi resimlerini buraya ekle

elif sayfa == "Neden Sen?":
    st.markdown('<h1 class="ana-baslik">Çünkü... ✨</h1>', unsafe_allow_index=True)
    
    sebepler = [
        "En kötü günümde bile beni güldürebildiğin için.",
        "Gözlerinin içine baktığımda huzuru bulduğum için.",
        "Sadece yanımda olman bile her şeyi güzelleştirdiği için.",
        "Hayallerime ortak olduğun için."
    ]
    
    for s in sebepler:
        st.markdown(f'<div class="not-kart">🌟 {s}</div>', unsafe_allow_index=True)

elif sayfa == "Küçük Bir Sürpriz":
    st.markdown('<h1 class="ana-baslik">Sana Bir Mesajım Var 💌</h1>', unsafe_allow_index=True)
    
    st.write("Aşağıdaki butona basmanı bekliyorum...")
    
    if st.button("Bana Tıkla! ✨"):
        st.balloons()
        st.snow()
        st.success("Seni her geçen gün daha çok seviyorum! ❤️")
        st.write("---")
        st.info("Bu site her zaman burada kalacak, tıpkı sana olan sevgim gibi.")

# Alt Bilgi
st.markdown("<br><br>", unsafe_allow_index=True)
st.caption("2026 | Senin için, seninle birlikte kodlandı.")
