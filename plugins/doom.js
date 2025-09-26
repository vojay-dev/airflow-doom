import GameComponent from "./game.js";

function DoomComponent() {
    return GameComponent({
        id: "doom-plugin-container",
        cssPath: "/doom/doom.css",
        zipPath: "/doom/doom.zip",
        exePath: "./DOOM/DOOM.EXE"
    });
}

globalThis["Doom"] = DoomComponent;
globalThis.AirflowPlugin = DoomComponent;
