def get_session():
    import streamlit as st
    if "language" not in st.session_state:
        st.session_state["language"] = "English"
    return st.session_state
