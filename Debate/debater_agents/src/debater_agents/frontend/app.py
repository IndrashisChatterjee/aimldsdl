import streamlit as st
import requests

# Read API base URL securely from Streamlit secrets
API_BASE = st.secrets.get("API_BASE")

st.title("DebaterAgents: AI Debate App")

topic = st.text_input("Enter a debate topic:")

if st.button("Start Debate") and topic:
    with st.spinner("Running debate..."):
        response = requests.post(f"{API_BASE}/debate",
            json={"topic": topic}
        )
        data = response.json()
        if "error" in data:
            st.error(data["error"])
        else:
            st.success("Debate complete")
            with st.expander("Propose Arguments"):
                st.markdown(data.get("propose", "No propose arguments found."))
            with st.expander("Oppose Arguments"):
                st.markdown(data.get("oppose", "No oppose arguments found."))
            with st.expander("Judge's Decision"):
                st.markdown(data.get("decide", "No decision found."))