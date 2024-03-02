import streamlit as st
import requests
import os

os.system("sudo apt update && sudo apt install ffmpeg")
# Set the title of the main page
st.title("Emotion Detector")

# Add elements to the sidebar

st.page_link(page="./pages/Text Input.py", label="Text to Emotion", icon="💬")
st.page_link(page="./pages/Audio_Input.py", label="Audio to Emotion", icon="🔉")
st.page_link(page="./pages/File Input.py", label="File to Emotion", icon="🗃")
st.page_link(page="./pages/Video_Upload.py", label="Video to Emotion", icon="🎥")
st.page_link(page="./pages/chat_input.py", label="Chat to Emotion", icon="🗣")

# from st_pages import hide_pages, show_pages, Page

# show_pages(
#     [
#         Page("Home.py"),
#         Page("pages/audio.py"),
#         Page("pages/Audio Input.py"),
#         Page("pages/Text Input.py"),
#     ]
# )

# hide_pages(
#     [
#         Page("pages/haarcascade_frontalface_default.xml"),
#      ]
# )
