import GameComponent from "./game.js";

function DoomComponent() {
    return GameComponent({
        id: "game-container",
        cssPath: "/gameflow/game.css",
        zipPath: "/gameflow/giana.zip",
        exePath: "./DOOMWEB.BAT"
    });
}

globalThis["Giana"] = DoomComponent;
globalThis.AirflowPlugin = DoomComponent;
