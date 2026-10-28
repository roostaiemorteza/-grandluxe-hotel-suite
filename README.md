# GrandLuxe V3 — Atlantis Royal Edition

Luxury hotel booking and suite configurator web app, packaged for offline asset loading in Streamlit and static deployment.

## Run with Streamlit
1. Install requirements: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`

`app.py` reads `index.html` and embeds the local Three.js, OrbitControls and Chart.js bundles into the page. The page also works as a standalone `index.html` when served from a web server with the included `js/` directory.

## Included
- `index.html` — hotel booking interface, 3D showcase and Atlantis Royal telemetry/backdrop effects.
- `app.py` — Streamlit entry point.
- `js/` — Three.js, OrbitControls, GLTFLoader and Chart.js.
- `netlify.toml`, `vercel.json`, `requirements.txt`, `.streamlit/config.toml` — deployment configuration.
