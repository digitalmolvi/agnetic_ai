# agnetic_ai_app.py
import streamlit as st
from src.ui.main_dashboard import show_dashboard

st.set_page_config(page_title="Agnetic AI Travel Assistant", layout="wide")

show_dashboard()