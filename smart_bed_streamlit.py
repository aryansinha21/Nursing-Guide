import streamlit as st
import time
import random
from datetime import datetime

if 'status' not in st.session_state:
    st.session_state.status = "Sleeping"

if 'last_updated' not in st.session_state:
    st.session_state.last_updated = datetime.now().strftime("%H:%M:%S")

def detect_patient_status():
    return "Awake" if random.random() < 0.1 else "Sleeping"

st.set_page_config(page_title="Smart Bed Sensor", layout="centered")
st.title("🛏️ Smart Bed Wake-Up Detector")
st.markdown("**Live patient status (simulated):**")

refresh_interval = 5
placeholder = st.empty()

while True:
    current_status = detect_patient_status()
    if current_status != st.session_state.status:
        st.session_state.status = current_status
        st.session_state.last_updated = datetime.now().strftime("%H:%M:%S")

    with placeholder.container():
        st.subheader(f"Status: `{st.session_state.status}`")
        st.write(f"Last updated: {st.session_state.last_updated}")
        st.progress(0)

    time.sleep(refresh_interval)
