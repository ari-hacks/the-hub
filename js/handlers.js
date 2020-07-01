function upload_file(ev) {
    var files = ev.target.files;
    var reader = new FileReader();
    reader.onload = function () {
        document.getElementById('output').innerHTML = reader.result;
        console.log(reader.result)
    };
    reader.readAsBinaryString(files[0]);
}
function process(ev) {
    console.log(ev.target.id)
    if (ev.target.id.includes('plot1')) {
        pyodide.runPython(`process_pie()`);
    } else if (ev.target.id.includes('plot2')) {
        pyodide.runPython(`process_scatter()`);
    } else if (ev.target.id.includes('plot3')) {
        pyodide.runPythonAsync(`process_time_series()`);
    } else if (ev.target.id.includes('plot4')) {
        pyodide.runPython(`process_geo_map()`);
    } else if (ev.target.id.includes('plot5')) {
        pyodide.runPython(`process_heat_maps()`);
    } else if (ev.target.id.includes('plot6')) {
        pyodide.runPython(`process_3d_maps()`);
    } else {
        pyodide.runPython(`print(no graph selected!)`);
    }
}

function clear(ev) {
    console.log(ev.target.id)
    if (ev.target.id.includes('plot1')) {
        document.getElementById("output").textContent = "";
        document.getElementById('input-plot1').value = "";
        Plotly.purge(document.getElementById("plot1"));

    } else if (ev.target.id.includes('plot2')) {
        document.getElementById("output").textContent = "";
        document.getElementById('input-plot2').value = "";
        Plotly.purge(document.getElementById("plot2"));

    } else if (ev.target.id.includes('plot3')) {
        document.getElementById("output").textContent = "";
        document.getElementById('input-plot3').value = "";
        Plotly.purge(document.getElementById("plot3"));

    } else if (ev.target.id.includes('plot4')) {
        document.getElementById("output").textContent = "";
        document.getElementById('input-plot4').value = "";
        Plotly.purge(document.getElementById("plot4"));

    } else if (ev.target.id.includes('plot5')) {
        document.getElementById("output").textContent = "";
        document.getElementById('input-plot5').value = "";
        Plotly.purge(document.getElementById("plot5"));

    } else if (ev.target.id.includes('plot6')) {
        document.getElementById("output").textContent = "";
        document.getElementById('input-plot6').value = "";
        Plotly.purge(document.getElementById("plot6"));
    } else {
        pyodide.runPython(`print(no graph selected!)`);
    }

}
