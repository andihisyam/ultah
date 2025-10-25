import streamlit as st
import random
import time
from streamlit_extras.let_it_rain import rain

# --- KONFIGURASI DASAR ---
st.set_page_config(page_title="🎂 Selamat Ulang Tahun Ratih!", page_icon="🎉", layout="centered")

# --- CSS TEMA TERANG (PINK PASTEL) ---
st.markdown("""
<style>
/* Warna latar belakang aplikasi */
[data-testid="stAppViewContainer"] {
    background-color: #fff5f8;
    color: #333333;
}

/* Header dan toolbar transparan */
[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: none;
}

/* Judul dan teks default */
h1, h2, h3, p, div {
    color: #333333 !important;
}

/* Kotak pesan */
.message-box {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 0px 15px rgba(255, 105, 180, 0.3);
    text-align: center;
    font-size: 18px;
    color: #333333;
}

/* Tombol utama */
div.stButton > button:first-child {
    background-color: white;
    color: #FF69B4;
    border-radius: 10px;
    border: 2px solid #FF69B4;
    font-weight: bold;
    font-size: 16px;
    padding: 8px 20px;
    transition: all 0.3s ease;
}

/* Efek hover tombol */
div.stButton > button:hover {
    background-color: #FF69B4;
    color: white;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --- STATE HALAMAN ---
if "page" not in st.session_state:
    st.session_state.page = "ucapan"

def go_to(page_name):
    st.session_state.page = page_name


# --- HALAMAN 1: UCAPAN UTAMA ---

if st.session_state.page == "ucapan":
    rain(emoji="🎈", font_size=40, falling_speed=5, animation_length=5)
    rain(emoji="🎉", font_size=35, falling_speed=3, animation_length=5)
    st.balloons()

    html_ucapan = """<h1 style='text-align:center; color:#FF69B4;'>🎂 SELAMAT ULANG TAHUN RATIH YANG KE-22 🎂</h1>
<div class='message-box'>
<p>Semoga di usia 22 tahun ini kamu semakin bahagia, kuat, dan penuh berkah 💖</p>
<p>Teruslah jadi pribadi yang ceria dan menyebarkan energi positif ke sekitar ✨</p>
<p>Dan selalu diberikan kesehatan dan keberkahan dalam menjalani Hidup 💌</p>
</div>"""

    st.markdown(html_ucapan, unsafe_allow_html=True)

    time.sleep(1.5)
    st.success(random.choice([
        "🎈 Jangan lupa tersenyum — kamu pantas bahagia!"
    ]))

    st.markdown("<br>", unsafe_allow_html=True)
    st.button("➡️ Next jika Kepo 💌", on_click=lambda: go_to("pesan"))



# --- HALAMAN 2: PESAN PANJANG ---
elif st.session_state.page == "pesan":
    html_pesan = """<h2 style='text-align:center; color:#FF69B4;'>💌 SURAT CINTA</h2>
<div class='message-box'>
<p>Ratih, selamat ulang tahun yang ke-22 🎂</p>

<p>22 tahun bukan sekadar angka. Itu adalah kumpulan momen, tawa, air mata, perjuangan, dan kebahagiaan yang sudah kamu lalui dengan luar biasa.
Kamu tumbuh menjadi pribadi yang kuat, penuh kasih, dan menginspirasi orang-orang di sekitarmu.</p>

<p>Di usia ini, semoga semua langkahmu selalu dipenuhi keberanian untuk mengejar mimpi.
Semoga kamu tidak pernah kehilangan senyum yang membuat dunia di sekitarmu terasa hangat.</p>

<p>Terima kasih sudah menjadi dirimu sendiri — apa adanya, tulus, dan selalu berusaha memberi yang terbaik.
Semoga kebahagiaan datang tanpa kamu minta, dan cinta selalu menemukanmu dan menemanimu di setiap perjalanan hidupmu. 💖</p>

<p style='text-align:center; font-weight:bold; color:#FF69B4; font-size:20px;'>
Selamat ulang tahun sekali lagi, Teman level 6 ku. Semoga kamu selalu bahagia dan Terus bareng aku wkwkwkw. 🌸
</p>
</div>"""

    st.markdown(html_pesan, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("⬅️ Kembali ke Ucapan 🎂", on_click=lambda: go_to("ucapan"))
