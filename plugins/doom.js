const { useRef, useEffect } = React;
const e = React.createElement;

function DoomComponent() {
    const rootRef = useRef(null);

    useEffect(() => {
        const styleLink = document.createElement("link");
        styleLink.rel = "stylesheet";
        styleLink.href = "/doom/doom.css";
        document.head.appendChild(styleLink);

        const jqueryScript = document.createElement("script");
        jqueryScript.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js";
        jqueryScript.async = true;
        document.body.appendChild(jqueryScript);

        jqueryScript.onload = () => {
            const dosScript = document.createElement("script");
            dosScript.src = "https://js-dos.com/cdn/js-dos-api.js";
            dosScript.async = true;
            document.body.appendChild(dosScript);

            dosScript.onload = () => {
                if (typeof window.emulators === "undefined") {
                    window.emulators = {};
                }
                window.emulators.pathPrefix = "/doom/";

                new window.Dosbox({
                    id: "doom-plugin-container",
                    onload: (dosbox) => dosbox.run("/doom/DOOM-@evilution.zip", "./DOOM/DOOM.EXE")
                });
            };
        };
    }, []);

    return e("div", { id: "doom-plugin-container", ref: rootRef });
}

globalThis["Doom"] = DoomComponent;
globalThis.AirflowPlugin = DoomComponent;
