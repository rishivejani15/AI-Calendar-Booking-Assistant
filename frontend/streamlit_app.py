import streamlit as st
import requests

st.title("📅 Calendar Booking Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask to book or check availability...")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    response = requests.post("https://ai-calendar-booking-assistant.streamlit.app/", json={"text": user_input})
    assistant_reply = response.json()["reply"]
    st.session_state.messages.append({"role": "assistant", "text": assistant_reply})

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["text"])
