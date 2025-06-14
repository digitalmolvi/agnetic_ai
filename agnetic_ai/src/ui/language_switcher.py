# src/ui/language_switcher.py
def language_switcher(session):
    import streamlit as st
    lang = st.sidebar.selectbox("🌐 Select Language", ["English", "Urdu"])
    session["language"] = lang