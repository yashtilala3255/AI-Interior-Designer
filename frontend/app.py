import requests
import streamlit as st

API_URL = st.secrets.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Interior Designer", page_icon="🏠", layout="wide")
st.title("AI Interior Designer 🏠✨")

mode = st.radio("Mode", ["Text to Image", "History"], horizontal=True)

if mode == "Text to Image":
    with st.form("generate_form"):
        prompt = st.text_input("Describe your room", "A cozy minimalist bedroom with warm lighting")
        room_type = st.selectbox("Room Type", ["bedroom", "living room", "kitchen", "office"])
        style = st.selectbox("Style", ["modern", "minimalist", "bohemian", "industrial"])
        colors = st.multiselect("Dominant Colors", ["white", "beige", "brown", "gray", "green", "blue"])
        submitted = st.form_submit_button("Generate")

    if submitted:
        payload = {
            "prompt": prompt,
            "room_type": room_type,
            "style": style,
            "colors": colors,
        }
        try:
            response = requests.post(f"{API_URL}/generate/text-to-image", json=payload, timeout=30)
            response.raise_for_status()
            st.success("Generation request succeeded")
            st.json(response.json())
        except Exception as exc:
            st.error(f"Request failed: {exc}")

if mode == "History":
    user_id = st.text_input("User ID", "demo-user")
    if st.button("Load History"):
        try:
            response = requests.get(f"{API_URL}/history/{user_id}", timeout=30)
            response.raise_for_status()
            st.json(response.json())
        except Exception as exc:
            st.error(f"Request failed: {exc}")
