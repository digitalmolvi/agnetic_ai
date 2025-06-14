# src/ui/emergency_panel.py
import streamlit as st
from src.utils.hospitals import find_nearby_hospitals


def emergency_panel():
    st.subheader("🚑 Nearest Hospitals")
    lat = st.number_input("Latitude", value=24.8607)
    lon = st.number_input("Longitude", value=67.0011)

    if st.button("Find Hospitals"):
        hospitals = find_nearby_hospitals(lat, lon)
        for h in hospitals:
            st.markdown(f"- **{h['name']}** ({h['distance_km']} km away)")
