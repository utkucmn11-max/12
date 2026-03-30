import streamlit as st

st.set_page_config(page_title="Bizim Hikayemiz", page_icon="❤️")

# Arka plan ve yazı tipleri için özel CSS
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    h1 { color: #ff4b4b; font-family: 'Arial'; text-align: center; }
    .stText { text-align: center; }
    </style>
    """, unsafe_allow_index=True)

st.title("Seni Sevmemin Binlerce Sebebi Var... ❤️")

tab1, tab2, tab3 = st.tabs(["Anılarımız", "Geri Sayım", "Notum"])

with tab1:
    st.header("📸 Galeri")
    # Buraya fotoğraflarınızı ekleyebilirsin
    st.image("https://via.placeholder.com/400", caption="İlk buluşmamız")

with tab2:
    st.header("⏳ Bir Sonraki Randevu")
    # Buraya bir sayaç kodu eklenebilir

with tab3:
    st.header("💌 Sana Mesajım")
    st.write("Buraya kalbinden geçen en güzel cümleleri yazabilirsin...")