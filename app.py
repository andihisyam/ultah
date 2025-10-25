import streamlit as st
import random
import time
from streamlit_extras.let_it_rain import rain

# --- KONFIGURASI DASAR ---
st.set_page_config(page_title="🎂 Selamat Ulang Tahun Ratih!", page_icon="🎉", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #fff5f8; /* pink pastel background */
        color: #333333;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #fff5f8;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- STATE HALAMAN ---
if "page" not in st.session_state:
    st.session_state.page = "ucapan"

def go_to(page_name):
    st.session_state.page = page_name

# --- HALAMAN 1: UCAPAN UTAMA ---
if st.session_state.page == "ucapan":
    # Animasi dan efek
    rain(emoji="🎈", font_size=40, falling_speed=5, animation_length=5)
    rain(emoji="🎉", font_size=35, falling_speed=3, animation_length=5)
    st.balloons()

    st.markdown("""
    <h1 style='text-align:center; color:#FF69B4;'>🎂 SELAMAT ULANG TAHUN RATIH YANG KE-22 🎂</h1>
    <div style='text-align:center; font-size:18px; background-color:rgba(255,255,255,0.8);
                padding:25px; border-radius:20px; box-shadow:0px 0px 20px rgba(255,105,180,0.4);'>
        <p>Hari ini istimewa banget karena kamu berulang tahun, Ratih! 🌸</p>
        <p>Semoga di usia 22 tahun ini kamu semakin bahagia, kuat, dan penuh berkah 💖</p>
        <p>Teruslah jadi pribadi yang ceria dan menyebarkan energi positif ke sekitar ✨</p>
        <p>Selamat menikmati hari spesialmu, kamu pantas mendapatkan yang terbaik! 🎁🎊</p>
    </div>
    """, unsafe_allow_html=True)

    # Pesan random tambahan
    time.sleep(1.5)
    st.success(random.choice([
        "🌟 Dunia sedang merayakan kamu hari ini!",
        "💐 Kamu luar biasa — tetap semangat dan percaya diri!",
        "🎈 Jangan lupa tersenyum — kamu pantas bahagia!",
        "💖 Tahun ke-22 ini akan jadi awal dari banyak hal indah!"
    ]))

    st.markdown("<br>", unsafe_allow_html=True)
    st.button("➡️ Next jika Kepo 💌", on_click=lambda: go_to("pesan"))


# --- HALAMAN 2: PESAN PANJANG ---
elif st.session_state.page == "pesan":
    html_pesan = """
    <h2 style='text-align:center; color:#FF69B4;'>💌 Pesan Panjang untuk Ratih</h2>
    <div style='font-size:18px; line-height:1.8; background-color:rgba(255,255,255,0.9);
                padding:25px; border-radius:20px; box-shadow:0px 0px 15px rgba(255,105,180,0.3);'>

    <p>Ratih, selamat ulang tahun yang ke-22 🎂</p>

    <p>22 tahun bukan sekadar angka. Itu adalah kumpulan momen, tawa, air mata, perjuangan, dan kebahagiaan yang sudah kamu lalui dengan luar biasa.
    Kamu tumbuh menjadi pribadi yang kuat, penuh kasih, dan menginspirasi orang-orang di sekitarmu.</p>

    <p>Di usia ini, semoga semua langkahmu selalu dipenuhi keberanian untuk mengejar mimpi.
    Semoga kamu tidak pernah kehilangan senyum yang membuat dunia di sekitarmu terasa hangat.</p>

    <p>Terima kasih sudah menjadi dirimu sendiri — apa adanya, tulus, dan selalu berusaha memberi yang terbaik untuk orang lain.
    Semoga kebahagiaan datang tanpa kamu minta, dan cinta selalu menemukanmu di setiap perjalanan hidupmu. 💖</p>

    <p style='text-align:center; font-weight:bold; color:#FF69B4; font-size:20px;'>
    Selamat ulang tahun sekali lagi, Ratih. Dunia lebih indah dengan adanya kamu. 🌸
    </p>

    </div>
    """
    st.markdown(html_pesan, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("⬅️ Kembali ke Ucapan 🎂", on_click=lambda: go_to("ucapan"))

