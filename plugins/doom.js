import GameComponent from "./game.js";

function DoomComponent() {
    return GameComponent({
        id: "game-container",
        cssPath: "/gameflow/game.css",
        zipPath: "/gameflow/doom.zip",
        exePath: "./DOOM/DOOM.EXE"
    });
}

globalThis["Doom"] = DoomComponent;
globalThis.AirflowPlugin = DoomComponent;
