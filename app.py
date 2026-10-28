"""
GrandLuxe Hotel & Suite — Smart Booking Engine & Management Suite
Streamlit Community Cloud entrypoint (main file: app.py).
Fully offline: inlines local Three.js & Chart.js from js/ directly into index.html
so that Streamlit Cloud iframe NEVER blocks or 404s on script assets.
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="GrandLuxe Hotel & Suite | Mediterranean",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<style>
  header, footer, #MainMenu {visibility: hidden !important;}
  .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
  html, body, .stApp {background: #0B0C10 !important; color: #F5F1E6;}
  iframe {border: none; width: 100% !important; min-height: 100vh;}
</style>""", unsafe_allow_html=True)

base_dir = Path(__file__).parent
html_content = (base_dir / "index.html").read_text(encoding="utf-8")

three_js_path = base_dir / "js" / "three.min.js"
chart_js_path = base_dir / "js" / "chart.umd.min.js"

# Inject Three.js inline
if three_js_path.exists():
    three_code = three_js_path.read_text(encoding="utf-8")
    if "<!-- INJECT_THREE_JS -->" in html_content:
        html_content = html_content.replace("<!-- INJECT_THREE_JS -->", f"<script>\n{three_code}\n</script>")
    else:
        html_content = html_content.replace('<script src="js/three.min.js"></script>', f"<script>\n{three_code}\n</script>")
        html_content = html_content.replace('<script src="https://cdn.jsdelivr.net/npm/three@0.158.0/build/three.min.js"></script>', f"<script>\n{three_code}\n</script>")

# Inject Chart.js inline
if chart_js_path.exists():
    chart_code = chart_js_path.read_text(encoding="utf-8")
    if "<!-- INJECT_CHART_JS -->" in html_content:
        html_content = html_content.replace("<!-- INJECT_CHART_JS -->", f"<script>\n{chart_code}\n</script>")
    else:
        html_content = html_content.replace('<script src="js/chart.umd.min.js"></script>', f"<script>\n{chart_code}\n</script>")
        html_content = html_content.replace('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>', f"<script>\n{chart_code}\n</script>")

components.html(html_content, height=1080, scrolling=True)
