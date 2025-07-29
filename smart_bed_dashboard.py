import streamlit as st
import time
import random
from datetime import datetime

# ------------------ Settings ------------------
st.set_page_config(page_title="Smart Bed Dashboard", page_icon="🛏️", layout="wide")

# ------------------ Functions ------------------
def detect_patient_status():
    return "Awake" if random.random() < 0.1 else "Sleeping"

def display_status():
    current_status = detect_patient_status()
    if current_status != st.session_state.status:
        st.session_state.status = current_status
        st.session_state.last_updated = datetime.now().strftime("%H:%M:%S")

    st.subheader("👀 Patient Status")

    if st.session_state.status == "Awake":
        st.success("✅ The patient is **Awake**")
    else:
        st.warning("😴 The patient is **Sleeping**")

    st.write(f"🕒 Last updated: {st.session_state.last_updated}")
    st.markdown("---")
    st.info("Auto-refresh every 5 seconds to update live status.")

def show_about():
    st.subheader("📌 About This Project")
    st.markdown("""
        **Smart Bed Wake-Up Detector** is a real-time monitoring system designed to assist families in observing when patients wake up from bed.  
        It can be extended to use real sensors, IoT, and even emergency alerts.

        - Built using **Python + Streamlit**
        - Ready for IoT hardware integration (like Raspberry Pi)
    """)

def show_contact():
    st.subheader("📞 Contact / Credits")
    st.markdown("""
        **Made by Aryan Sinhaa**  
        GitHub: [@aryansinha21](https://github.com/aryansinha21)  
        Email: *youremail@example.com*  
    """)

# ------------------ Sidebar ------------------
menu = st.sidebar.radio(
    "📋 Menu",
    ["Live Status", "About Project", "Contact / Credits"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("🚀 Made with ❤️ by **Aryan Sinhaa**")
st.sidebar.caption("Version 1.0")

# ------------------ App State Init ------------------
if 'status' not in st.session_state:
    st.session_state.status = "Sleeping"
if 'last_updated' not in st.session_state:
    st.session_state.last_updated = datetime.now().strftime("%H:%M:%S")

# ------------------ Main Display ------------------
if menu == "Live Status":
    placeholder = st.empty()
    while True:
        with placeholder.container():
            display_status()
        time.sleep(5)

elif menu == "About Project":
    show_about()

elif menu == "Contact / Credits":
    show_contact()

# ------------------ Footer ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">🛏️ Smart Bed Sensor © 2025 | Developed by <strong>Aryan Sinhaa</strong></p>', unsafe_allow_html=True)
