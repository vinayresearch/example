# hello_world_weather.py

import streamlit as st
from datetime import datetime
from streamlit_folium import st_folium
import folium
import numpy as np

st.set_page_config(page_title="Hello Weather AI", layout="centered")

st.title("🌦️ Hello Weather AI Demo")

# --- 1. Input from User ---
st.subheader("🗓️ Choose date and time")
date = st.date_input("Select a date", datetime.today())
time = st.time_input("Select time", datetime.now().time())

st.subheader("📍 Pick location on map")
m = folium.Map(location=[20, 78], zoom_start=2)
map_data = st_folium(m, height=300, width=700)
lat, lon = 0.0, 0.0
if map_data["last_clicked"]:
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    st.success(f"Selected location: {lat:.2f}, {lon:.2f}")

# --- 2. Simulated Atmospheric Prediction ---
if lat and lon:
    st.subheader("🧠 Simulated Atmospheric Predictions")

    # Use datetime and location to simulate predictions
    seed = int(lat * lon * 1000 + date.day + time.hour)
    rng = np.random.default_rng(seed)
    
    temp = round(rng.uniform(20, 45), 2)  # °C
    humidity = round(rng.uniform(10, 90), 1)  # %
    rainfall = round(rng.exponential(10), 1)  # mm
    heatwave_intensity = max(0, temp - 35)  # °C above threshold

    st.metric("🌡️ Temperature (°C)", temp)
    st.metric("💧 Humidity (%)", humidity)
    st.metric("🌧️ Rainfall Amount (mm)", rainfall)
    st.metric("🔥 Heatwave Intensity (°C above 35°C)", heatwave_intensity)

    # --- 3. Generate Summary ---
    st.subheader("📢 Weather Summary")

    if heatwave_intensity > 5:
        st.warning("Severe heatwave likely. Avoid outdoor exposure.")
    elif rainfall > 20:
        st.info("Heavy rainfall expected. Carry protection.")
    elif temp < 15:
        st.info("Cold day expected. Dress warmly.")
    else:
        st.success("Mild weather expected. No extremes predicted.")
