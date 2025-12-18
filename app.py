
import streamlit as st
import requests

API_URL = "http://localhost:8000/recommend"

st.title("SHL GenAI Recommender")

query = st.text_area("Enter job description")
if st.button("Recommend"):
    res = requests.post(API_URL, json={"query":query}).json()
    for r in res["recommended_assessments"]:
        st.subheader(r["name"])
        st.write(r["description"])
