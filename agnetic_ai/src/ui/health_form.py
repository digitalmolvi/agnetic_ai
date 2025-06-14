import streamlit as st

def health_risk_form():
    st.subheader("🩺 Health Risk Calculator")
    age = st.number_input("Age", min_value=1)
    has_chronic = st.checkbox("Chronic Conditions")
    smoker = st.checkbox("Smoker")

    risk = "Low"
    if age > 60 or has_chronic or smoker:
        risk = "High"
    elif age > 40:
        risk = "Medium"

    st.markdown(f"**Risk Level:** {risk}")

