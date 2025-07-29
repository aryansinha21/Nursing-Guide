import streamlit as st
import time
import random
from datetime import datetime

# ------------------ Page Setup ------------------
st.set_page_config(page_title="Smart Bed Dashboard", page_icon="🛏️", layout="wide")

# ------------------ Session State Init ------------------
if 'status' not in st.session_state:
    st.session_state.status = "Sleeping"
if 'last_updated' not in st.session_state:
    st.session_state.last_updated = datetime.now().strftime("%H:%M:%S")

# ------------------ Simulated Sensor Function ------------------
def detect_patient_status():
    # Simulate sensor: 10% chance of "Awake"
    return "Awake" if random.random() < 0.1 else "Sleeping"

# ------------------ Sidebar Menu ------------------
menu = st.sidebar.radio("📋 Menu", ["Live Status", "About Project", "Contact / Credits"])
st.sidebar.markdown("---")
st.sidebar.markdown("👨‍💻 Made by **Aryan Sinhaa**")
st.sidebar.caption("Version 1.0")

# ------------------ Live Status Page ------------------
if menu == "Live Status":
    st.title("🛏️ Smart Bed Wake-Up Detector")
    st.markdown("Monitoring real-time patient status...")

    placeholder = st.empty()
    refresh_interval = 5  # seconds

    while True:
        current_status = detect_patient_status()

        if current_status != st.session_state.status:
            st.session_state.status = current_status
            st.session_state.last_updated = datetime.now().strftime("%H:%M:%S")

        with placeholder.container():
            st.subheader("👀 Patient Status")

            if st.session_state.status == "Awake":
                st.success("✅ The patient is **Awake**")
            else:
                st.warning("😴 The patient is **Sleeping**")

            st.markdown(f"🕒 Last updated: `{st.session_state.last_updated}`")
            st.info("Auto-refresh every 5 seconds")

        time.sleep(refresh_interval)

# ------------------ About Page ------------------
elif menu == "About Project":
    st.title("📌 About This Project")
    st.markdown("""
    **Smart Bed Wake-Up Detector** is a prototype that simulates real-time monitoring of patients in bed.  
    Designed to assist family members and caregivers, it detects when a patient wakes up using motion or pressure sensors (or simulation).
    
    ### Key Features:
    - Live patient status display
    - Auto-refreshing dashboard
    - Easy integration with sensors (like Raspberry Pi, ESP32)
    - Ready for alerts (email, SMS, app notifications)

    This system can help prevent falls, missed medication times, or unnoticed emergencies.
    """)

# ------------------ Contact Page ------------------
elif menu == "Contact / Credits":
    st.title("📞 Contact / Credits")
    st.markdown("""
    - **Developer:** Aryan Sinhaa  
    - **GitHub:** [@aryansinha21](https://github.com/aryansinha21)  
    - **Email:** *your-email@example.com*  
    - **Technology Used:** Python, Streamlit  
    - **License:** MIT License
    """)

# ------------------ Footer ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">🛏️ Smart Bed Sensor © 2025 | Developed by <strong>Aryan Sinhaa</strong></p>', unsafe_allow_html=True)
