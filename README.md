# GrandLuxe Hotel & Suite — Smart Booking Engine & Management Suite ✨

Ultra-luxury single-page hotel booking & HMS platform (deep obsidian `#0B0C10` + champagne gold `#D4AF37`, frosted dark glassmorphism) featuring:

- 🌌 **3D motion graphics** — Three.js hero banner (drag 360°, auto-rotate, floating micro-interactions) + interactive **3D Room Configurator** (live lighting, window view, VIP add-ons on the 3D model)
- 🎬 **Cinematic background video bands** for Spa, Fine Dining and Private Beach sections
- 🌍 **Live 5-language i18n** (EN / TR / RU / DE / AR) with instant **RTL layout for Arabic** — no page reload
- 🔎 **Smart room search engine** (check-in/out calendar, guests, suite type) + **live multi-currency converter** (₺ / € / $ / ₽)
- 🛥️ **VIP Experience Add-ons** (luxury airport transfer GZP/AYT, private yacht tour, Ottoman hammam spa) with a live itemized invoice
- 🤖 **AI Concierge bot** — 24/7 multilingual chat with **voice input (SpeechRecognition)** and **voice output (speechSynthesis)**
- 🅰️ **Hotelier & Front Desk dashboard** — interactive room-rack calendar (Available/Occupied/Cleaning/Reserved), reservation management, occupancy & revenue analytics (Chart.js), VIP/AI request queue
- 🅱️ **Platform CMS & Technical Customizer** — create/edit/delete/reorder room cards, customize hero & 3D banner texts, Media Showcase Hub (drag & drop video/images), and a live 5-language i18n dictionary editor

## Files
| File | Purpose |
|---|---|
| `index.html` | The complete suite (standalone single file) |
| `app.py` | Streamlit Community Cloud entrypoint |
| `requirements.txt` | Python dependencies (Streamlit only) |
| `.streamlit/config.toml` | Streamlit luxury dark theme & server config |
| `vercel.json` | Static deployment config for Vercel |
| `netlify.toml` | Static deployment config for Netlify |

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Or simply open `index.html` in any modern browser (works fully offline except CDN fonts/Three.js/Chart.js).

## Deploy on Streamlit Community Cloud (streamlit.io / share.streamlit.io)
1. Put this folder in a **public GitHub repository** (must include `app.py`, `index.html`, `requirements.txt`, `.streamlit/config.toml`).
2. Go to **https://share.streamlit.io** and sign in with your GitHub account.
3. Click **“Create app” → “Deploy a public app from GitHub”**.
4. Repository: select your repo — Branch: `main` — **Main file path: `app.py`**.
5. (Optional) App URL: e.g. `grandluxe-hotel-suite`.
6. Click **Deploy!**. Streamlit installs `streamlit>=1.36.0` from `requirements.txt` and serves the suite.
7. Any `git push` to `main` auto-redeploys the live app.

## Deploy on Vercel
1. Push to GitHub → import the repo at **vercel.com/new**.
2. Framework Preset: **Other** (static) — `vercel.json` is already included, no build command needed.
3. Deploy — the site is served from `index.html`.

## Deploy on Netlify
1. Push to GitHub → **app.netlify.com → Add new site → Import an existing project**.
2. Build command: none; publish directory: repo root (`netlify.toml` included, SPA-style redirect configured).
3. Deploy.

## Admin access
Use the top navigation to switch between the **Hotelier Panel** and the **CMS Panel** (role badge visible in the header).
