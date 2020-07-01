function executePython() {
    languagePluginLoader.then(() => {
        var req = new XMLHttpRequest();
        
        function reqListener() {
            if (this.status != 200) {
                console.error("Could not load python");
            } else {
                pyodide.loadPackage(["numpy", "matplotlib"]).then(() => {
                    pyodide.runPythonAsync(this.responseText).then(() => {
                        pyodide.runPythonAsync(`run()`);
                    });
                });
            }
        }

        req.open("GET", "py/build.py");
        req.addEventListener("load", reqListener)
        req.send();
    });
}
