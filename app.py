import streamlit as st
import google.generativeai as genai

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Asep AI - Hiburan & Teman Gabut",
    page_icon="😎",
    layout="centered"
)

# Judul dan Sambutan Khas Asep AI
st.title("😎 Asep AI - Teman Gabut & Hiburan")
st.write("Sini, Bro! Mau ngobrol santai, cari bahan lelucon, atau sekadar ngelepas penat? Aman, semua bisa diobrolin di sini.")

# Inisialisasi API Key menggunakan cara klasik yang paling stabil
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Menggunakan model klasik yang stabil untuk obrolan santai
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Waduh Bro, ada kendala konfigurasi API Key: {e}")
    st.stop()

# Sistem instruksi khusus karakter Asep AI yang fokus menghibur
system_instruction = """
Lu adalah Asep AI, temen ngobrol virtual yang asik, lucu, santai, dan jago banget menghibur orang yang lagi gabut atau penat. 
Gunakan gaya bahasa tongkrongan yang akrab, panggil pengguna dengan sebutan 'bro', pakai kata-kata seperti 'woles', 'gaskeun', 'mantap'. 
Tujuan utama lu adalah bikin pengguna senyum, ketawa, atau ngerasa ditemenin lewat obrolan yang seru dan humoris.
"""

# Simpan riwayat chat di memori sesi Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan pesan chat sebelumnya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kolom ngetik pesan chat
if user_input := st.chat_input("Mau ngobrol atau ngebahas apa nih, Bro?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Kirim ke model Gemini untuk dapetin balasan yang menghibur
    try:
        full_prompt = f"{system_instruction}\n\nUser: {user_input}"
        response = model.generate_content(full_prompt)
        ai_reply = response.text
    except Exception as e:
        ai_reply = f"Waduh Bro, sinyalnya lagi agak ngadat nih: {e}"

    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
