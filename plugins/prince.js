import GameComponent from "./game.js";

function PrinceComponent() {
    return GameComponent({
        id: "game-container",
        cssPath: "/gameflow/game.css",
        zipPath: "/gameflow/prince.zip",
        exePath: "./Prince\ of\ Persia/PRINCE.EXE"
    });
}

globalThis["Prince"] = PrinceComponent;
globalThis.AirflowPlugin = PrinceComponent;
