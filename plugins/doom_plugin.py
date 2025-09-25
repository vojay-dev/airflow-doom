from pathlib import Path

from airflow.plugins_manager import AirflowPlugin
from fastapi import FastAPI
from fastapi.responses import FileResponse

PLUGIN_DIR = Path(__file__).parent
app = FastAPI(title="Doom", version="0.1.0")

@app.get("/wdosbox.js")
async def serve_wdosbox_worker():
    return FileResponse(
        path=str(PLUGIN_DIR / "wdosbox.js"),
        media_type="application/javascript",
        filename="wdosbox.js",
    )

@app.get("/wdosbox.wasm")
async def serve_wdosbox_wasm():
    return FileResponse(
        path=str(PLUGIN_DIR / "wdosbox.wasm"),
        media_type="application/wasm",
        filename="wdosbox.wasm",
    )

@app.get("/DOOM-@evilution.zip")
async def serve_doom_zip():
    return FileResponse(
        path=str(PLUGIN_DIR / "DOOM-@evilution.zip"),
        media_type="application/zip",
        filename="DOOM-@evilution.zip",
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

