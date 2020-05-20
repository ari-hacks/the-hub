# Data Hub 📈

![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)


## About

A demo hub where users can experiment with data science by graphing data sets in the browser then downloading them. Web Monetized browsers won't see the ads on the page and can also experiment with additional graphing tools.


## Features

- [x] csv upload 
- [x] Enhanced Plots with [Plotly](https://plotly.com/)
- [x] Web Monetization enabled 
- [x] Image download 

## Testing Data

Plot | Input File 
---------|----------
 Pie | [Comparison of trending operating systems](/data/os-comparison.csv) | 
 Scatter/Line | [Trends of funny zoom backgrounds](/data/zoom-backgrounds.csv) | 
 Time Series | [Comparison of trending noodles](/data/Pho%20vs%20Ramen%20vs%20Soba.csv) | 
 Geo Map | [International certain earthquake data](/data/earthquake-data.csv) | 
 Heat Map | [Random Data Set](/data/heatmap-dataset%20-%20Sheet1.csv) | 
 3-D | [Random Data set](/data/plotly-dataset.csv) 

## Set up

### Requirements

- [Python](https://www.python.org/) 3.7
- Pipenv
- Browser with [coil wallet (No Sign in required for testing)](https://chrome.google.com/webstore/detail/coil/locbifcbeldmnphbgkdigjmkbfkhbnca?hl=en) 
- [Pyodide Downloaded](https://github.com/iodide-project/pyodide/releases)
- [Bookmarklet : For testing coil without an account](https://testwebmonetization.com/)
  


### Local development

After the above requirements have been met:

 
1.  Clone this repository and `cd` into it

    ```bash
    ➜ git clone https://github.com/ari-hacks/the-hub.git
    ➜ cd the-hub
    ```
2.  Dependencies 

    ```bash
    ➜ pipenv shell
    ➜ pipenv install
    ```
3.  Run the server

    ```bash
    ➜ python3 server.py
    #navigate to http://127.0.0.1:8000/
    ```

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.