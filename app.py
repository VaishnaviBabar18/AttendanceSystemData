import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Get current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Set page title and header
st.set_page_config(page_title="Attendance Data", layout="centered")
st.title("Attendance Data")
st.subheader(f"📅 Date: {date} | 🕒 Time: {timestamp}")

# Autorefresh every 2 seconds
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# Display FizzBuzz logic
with st.container():
    st.markdown("### 🔁 Counter Output:")
    if count == 0:
        st.success("🚀 Count is zero")
    elif count % 3 == 0 and count % 5 == 0:
        st.warning("🎉 FizzBuzz")
    elif count % 3 == 0:
        st.info("✨ Fizz")
    elif count % 5 == 0:
        st.info("💥 Buzz")
    else:
        st.write(f"🔢 Count: {count}")

# Display attendance data
try:
    df = pd.read_csv(f"Attendance/Attendance_{date}.csv")
    st.markdown("### 📋 Attendance Sheet:")
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.error(f"❌ Attendance file for {date} not found.")
