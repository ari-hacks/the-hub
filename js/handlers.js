function upload_file(ev) {
    var tgt = ev.target;
    var files = tgt.files;
              var reader = new FileReader();
              reader.onload = function () {
                  document.getElementById('output').innerHTML = reader.result;
                  //parse this into csv or json? Need to be able to read this better
                  console.log(reader.result)
                  //pyodide.runPythonAsync(`process_upload(`+ reader.result +`)`);
               };
             reader.readAsBinaryString(files[0]);
}
function process(ev) {
    var tgt = ev.target
    console.log(tgt)
    //passed on which id triggered the event logic loop to pick which method to run
    pyodide.runPython(`process_upload()`);
}

function clear(ev) {
    //add logic to handle clear for different plots 
    document.getElementById("output").textContent = ""; 
    document.getElementById('input-plot1').value = "";
    Plotly.purge(document.getElementById("plot1"));



}
