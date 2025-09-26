from pathlib import Path

import requests
from airflow.plugins_manager import AirflowPlugin
from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse

PLUGIN_DIR = Path(__file__).parent
app = FastAPI(title="Doom", version="0.1.0")

@app.get("/DOOM-@evilution.zip")
async def serve_doom_zip():
    url = "https://github.com/thedoggybrad/doom_on_js-dos/raw/refs/heads/main/DOOM-@evilution.zip"
    r = requests.get(url, stream=True)
    r.raise_for_status()

    return StreamingResponse(
        r.iter_content(chunk_size=8192),
        media_type="application/zip",
        headers={
            "Content-Disposition": 'attachment; filename="DOOM-@evilution.zip"',
            "Access-Control-Allow-Origin": "*",
        },
    )

@app.get("/doom.css")
async def serve_doom_css():
    return FileResponse(
        path=str(PLUGIN_DIR / "doom.css"),
        media_type="text/css",
        filename="doom.css",
    )

@app.get("/doom.js")
async def serve_react_component():
    return FileResponse(
        path=str(PLUGIN_DIR / "doom.js"),
        media_type="application/javascript",
        filename="doom.js",
    )

@app.get("/")
async def root():
    return { "message": "Doom Plugin Active" }

class DoomPlugin(AirflowPlugin):
    name = "doom"
    fastapi_apps = [{"app": app, "url_prefix": "/doom", "name": "Doom"}]
    react_apps = [{
        "name": "Doom",
        "bundle_url": "/doom/doom.js",
        "destination": "dag",
        "url_route": "doom",
    }]
