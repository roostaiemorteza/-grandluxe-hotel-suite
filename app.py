"""
GrandLuxe Hotel & Suite — Smart Booking Engine & Management Suite
Streamlit Community Cloud entrypoint (main file: app.py).
Serves the full single-page suite (index.html) with the luxury dark theme.
Run locally:  streamlit run app.py
Deploy:       push to GitHub -> share.streamlit.io -> Main file path: app.py
"""
import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GrandLuxe Hotel & Suite | Smart Booking & HMS",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<style>
  header, footer {visibility: hidden !important;}
  #MainMenu {visibility: hidden !important;}
  .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
  html, body, .stApp {background: #0B0C10 !important; color: #F5F1E6;}
  iframe {border: none;}
</style>""", unsafe_allow_html=True)

html = (pathlib.Path(__file__).parent / "index.html").read_text(encoding="utf-8")
st.components.v1.html(html, height=900, scrolling=True)
