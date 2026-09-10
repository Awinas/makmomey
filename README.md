# Mak Momey AI Web Prototype v1

Localhost-first web prototype. It includes chat, demo Mak-style replies, browser speech input/output, local memory, settings, and a FastAPI backend.

## Run
1. Install Python 3.11+.
2. In `backend`:
   `py -m venv .venv`
   `.\.venv\Scripts\Activate.ps1`
   `pip install -r requirements.txt`
3. Start:
   `uvicorn server:app --reload --host 127.0.0.1 --port 8000`
4. In another terminal:
   `py -m http.server 5500 --directory frontend`
5. Open `http://127.0.0.1:5500`

API keys must remain server-side. This prototype does not include real voice cloning yet.
