# src/ui/main_dashboard.py
import streamlit as st
from src.ui.language_switcher import language_switcher
from src.ui.health_form import health_risk_form
from src.ui.emergency_panel import emergency_panel
from src.utils.session import get_session


def show_dashboard():
    session = get_session()
    language_switcher(session)
    st.title("🗺️ Agnetic AI Travel Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.header("🩺 Health Check")
        health_risk_form()

    with col2:
        st.header("🚨 Emergency Access")
        emergency_panel()
