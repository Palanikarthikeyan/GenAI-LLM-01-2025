import streamlit as st
import time
st.balloons()  # Celebration balloons
st.progress(50)  # Progress bar
with st.spinner('Wait for it...'):
    time.sleep(2)  # Simulating a process delay
