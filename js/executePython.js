
//Function that takes the main python file and loads it to execute via pyodide
function executePython() {
    languagePluginLoader.then(() => {
        console.log(pyodide.runPython(`import sys\nsys.version`));
        var req = new XMLHttpRequest();
        req.open("GET", "py/build.py");
        req.addEventListener("load", () => {
            if (req.status != 200) {
                console.error("Could not load python");
            } else {
                    pyodide.loadPackage(["micropip", "numpy", "matplotlib"]).then(() => {
                    pyodide.runPythonAsync(req.responseText).then(() => {
                    pyodide.runPythonAsync(`run()`);
                    });
                });
            }
        });
        req.send();
    });
}
