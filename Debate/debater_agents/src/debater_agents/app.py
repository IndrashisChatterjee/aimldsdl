import streamlit as st
import requests

st.title("DebaterAgents: AI Debate App")

topic = st.text_input("Enter a debate topic:")

if st.button("Start Debate") and topic:
    with st.spinner("Running debate..."):
        response = requests.post(
            "http://localhost:8000/debate",
            json={"topic": topic}
        )
        data = response.json()
        if "error" in data:
            st.error(data["error"])
        else:
            st.subheader("Propose Arguments")
            st.markdown(data.get("propose", "No oppose arguments found."))
            st.subheader("Oppose Arguments")
            st.markdown(data.get("oppose", "No oppose arguments found."))
            st.subheader("Judge's Decision")
            st.markdown(data.get("decide", "No decision found."))