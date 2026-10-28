"""GrandLuxe V3 — Atlantis Royal Edition, offline Streamlit entry point."""
from pathlib import Path
import re
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="GrandLuxe | Atlantis Royal Edition", page_icon="✨", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>header,footer,#MainMenu{visibility:hidden!important}.block-container{padding:0!important;margin:0!important;max-width:100%!important}html,body,.stApp{background:#0B0C10!important;color:#F5F1E6}iframe{border:0;width:100%!important;min-height:100vh}</style>""",unsafe_allow_html=True)
base=Path(__file__).parent
html=(base/"index.html").read_text(encoding="utf-8")
# Remove external local-file script elements before embedding their contents.
for name in ("three.min.js","OrbitControls.js","chart.umd.min.js"):
    html=re.sub(r'<script\s+src=["\']js/'+re.escape(name)+r'["\']\s*>\s*</script>',"",html,flags=re.I)
three=(base/"js"/"three.min.js").read_text(encoding="utf-8")
orbit=(base/"js"/"OrbitControls.js").read_text(encoding="utf-8")
chart=(base/"js"/"chart.umd.min.js").read_text(encoding="utf-8")
html=html.replace("<!-- INJECT_THREE_JS -->", "<script>\n"+three+"\n</script><script>\n"+orbit+"\n</script>")
html=html.replace("<!-- INJECT_CHART_JS -->", "<script>\n"+chart+"\n</script>")
components.html(html,height=1080,scrolling=True)
