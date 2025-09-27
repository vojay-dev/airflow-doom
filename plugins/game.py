from pathlib import Path

import requests
from airflow.plugins_manager import AirflowPlugin
from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse

PLUGIN_DIR = Path(__file__).parent
app = FastAPI(title="GameFlow", version="0.1.0")

# all game images used are shareware or freeware

@app.get("/doom.zip")
async def serve_doom_zip():
    url = "https://image.dosgamesarchive.com/games/doom-box.zip"
    r = requests.get(url, stream=True)
    r.raise_for_status()

    return StreamingResponse(
        r.iter_content(chunk_size=8192),
        media_type="application/zip",
        headers={
            "Content-Disposition": 'attachment; filename="doom.zip"',
            "Access-Control-Allow-Origin": "*",
        },
    )

@app.get("/giana.zip")
async def serve_prince_zip():
    url = "https://image.dosgamesarchive.com/games/giana-gus.zip"
    r = requests.get(url, stream=True)
    r.raise_for_status()

    return StreamingResponse(
        r.iter_content(chunk_size=8192),
        media_type="application/zip",
        headers={
            "Content-Disposition": 'attachment; filename="giana.zip"',
            "Access-Control-Allow-Origin": "*",
        },
    )

@app.get("/game.css")
async def serve_doom_css():
    return FileResponse(
        path=str(PLUGIN_DIR / "game.css"),
        media_type="text/css",
        filename="game.css",
    )

@app.get("/game.js")
async def serve_game_component():
    return FileResponse(
        path=str(PLUGIN_DIR / "game.js"),
        media_type="application/javascript",
        filename="game.js",
    )

@app.get("/doom.js")
async def serve_doom_component():
    return FileResponse(
        path=str(PLUGIN_DIR / "doom.js"),
        media_type="application/javascript",
        filename="doom.js",
    )

@app.get("/giana.js")
async def serve_doom_component():
    return FileResponse(
        path=str(PLUGIN_DIR / "giana.js"),
        media_type="application/javascript",
        filename="doom.js",
    )

@app.get("/placeholder.jpg")
async def serve_placeholder_image():
    return FileResponse(
        path=str(PLUGIN_DIR / "placeholder.jpg"),
        media_type="image/jpeg",
        filename="placeholder.jpg",
    )

@app.get("/")
async def root():
    return { "message": "GameFlow Plugin Active" }

class GameFlow(AirflowPlugin):
    name = "GameFlow"
    fastapi_apps = [{"app": app, "url_prefix": "/gameflow", "name": "GameFlow"}]
    react_apps = [{
        "name": "Doom",
        "bundle_url": "/gameflow/doom.js",
        "destination": "nav",
        "url_route": "doom",
    }, {
        "name": "Giana Sisters",
        "bundle_url": "/gameflow/giana.js",
        "destination": "nav",
        "url_route": "giana",
    }]
