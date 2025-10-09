import streamlit as st
import requests

# Read API base URL securely from Streamlit secrets
API_BASE = st.secrets.get("API_BASE")


st.title("Finance Agent")

company = st.text_input("Enter company name:")

if st.button("Run Crew"):
    with st.spinner("Processing..."):
        response = requests.post(
            f"{API_BASE}/run_crew",
            json={"company": company}
        )
    if response.status_code == 200:
        result = response.json()["result"]
        with st.expander("View Output Report"):
            st.markdown(result)
    else:
        st.error(f"Error: {response.text}")