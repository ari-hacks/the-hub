from js import document, Plotly,console
import logging
import pandas as pd
import numpy as np
import csv
import sys

logging.basicConfig(level=logging.INFO)

def load():
    document.getElementById('load-python').classList.add('alert-success')
    document.getElementById('load-python').innerHTML = 'Python Loaded'

def process_input():
    """
    Get data and set the header - return array 
    """
    rows = []
    file_data = document.getElementById("output").textContent
    logging.info(file_data) 
     
    csv_reader = csv.reader(file_data.splitlines())
    for row in csv_reader:
        logging.info(row)
        rows.append(row)
        
    df = pd.DataFrame(data=rows)
    set_header = df.iloc[0] 
    df = df[1:] 
    df.columns = set_header
    logging.info(df)
    return df 
    
def process_scatter():
    df = process_input()
    col1 = df[df.columns[0]].values
    col2 = df[df.columns[1]].values
 
    Plotly.plot(document.getElementById('plot2'),
            [{'x':col1, 'y': col2,
            'type': 'scatter',
            'mode': 'markers+lines',
            'hoverinfo': 'label',
            'label': 'Zoom Background Interest'
            }])

def process_pie():
    df = process_input()
    
    df[df.columns[1]] =pd.to_numeric(df[df.columns[1]])
    df[df.columns[2]] =pd.to_numeric(df[df.columns[2]])
    df[df.columns[3]] =pd.to_numeric(df[df.columns[3]])
    col1 = df[df.columns[1]].values
    col2 = df[df.columns[2]].values
    col3 = df[df.columns[3]].values
  
    Plotly.plot(document.getElementById('plot1'),
            [{
            'values': [df[df.columns[1]].sum(),df[df.columns[2]].sum(),df[df.columns[3]].sum()],
            'labels':[df[df.columns[1]].name,df[df.columns[2]].name,df[df.columns[3]].name],
            'type': 'pie'
            }],
            {'title': 'Basic Pie Chart'})
            # {  'height': 400,'width': 500})
    
 
def process_time_series():
    df = process_input()
   
    df[df.columns[1]] =pd.to_numeric(df[df.columns[1]])
    df[df.columns[2]] =pd.to_numeric(df[df.columns[2]])
    df[df.columns[3]] =pd.to_numeric(df[df.columns[3]])
    
    col1 = df[df.columns[0]].values
    col2 = df[df.columns[1]].values
    col3 = df[df.columns[2]].values
    col4 = df[df.columns[3]].values
    
    Plotly.plot(document.getElementById('plot3'),
        [{
            'x':col1 ,
            'y':col2, 
            'type': 'scatter',
            'mode': "lines",
            'name': 'Pho',
            'line': {'color': '#17BECF'}
            },
             {
            'x':col1,
            'y':col3, 
            'type': "scatter",
            'mode': "lines",
            'name': 'Ramen',
            'line': {'color': '#7F7F7F'}
            },
              {
            'x': col1,
            'y': col4, 
            'type': "scatter",
            'mode': "lines",
            'name': 'Soba',
            'line': {'color': '#7C19E2'}
        }])

    

def process_geo_map():
    df = process_input()
   
    df[df.columns[1]] =pd.to_numeric(df[df.columns[1]])
    df[df.columns[2]] =pd.to_numeric(df[df.columns[2]])
    
    col1 = df[df.columns[1]].values
    col2 = df[df.columns[2]].values
    col3 = df[df.columns[13]].values
    Plotly.plot(document.getElementById('plot4'),
     [{
    'type': 'scattergeo',
    'lon' : col2,
    'lat': col1,
    'text' : col3}] )



def process_heat_maps():
    df = process_input()
    
    df[df.columns[0]] =pd.to_numeric(df[df.columns[0]])
    df[df.columns[1]] =pd.to_numeric(df[df.columns[1]])
    df[df.columns[2]] =pd.to_numeric(df[df.columns[2]])
    
    col0 = df[df.columns[0]].values
    col1 = df[df.columns[1]].values
    col2 = df[df.columns[2]].values
    col3 = df[df.columns[3]].values
    col4 = df[df.columns[4]].values

    Plotly.plot(document.getElementById('plot5'),
     [{ 'z': [col0, col1, col2],
        'x': col3,
        'y': col4,
        'type': 'heatmap',
        'hoverongaps': 'false'
            }],
            {'title': 'Basic Heat Map'})

 

def process_3d_maps():
    df = process_input()

    col0 = df[df.columns[0]].values
    col1 = df[df.columns[1]].values
    col2 = df[df.columns[2]].values
    col3 = df[df.columns[3]].values
    col4 = df[df.columns[4]].values
    col5= df[df.columns[5]].values
     
    Plotly.plot(document.getElementById('plot6'),
        [ {
	    'x':col0,
        'y':col1 ,
        'z': col2,
	    'mode': 'markers',
	    'marker': {
		    'size': 12,
		    'line': {
		    'color': 'rgba(217, 217, 217, 0.14)',
		    'width': 0.5},
		    'opacity': 0.8},
	    'type': 'scatter3d'
        },
         {
	'x':col3,
    'y': col4,
    'z': col5,
	'mode': 'markers',
	'marker': {
		'color': 'rgb(127, 127, 127)',
		'size': 12,
		'symbol': 'circle',
		'line': {
		'color': 'rgb(204, 204, 204)',
		'width': 1},
		'opacity': 0.8},
	'type': 'scatter3d'}],
        {'margin': {
	    'l': 0,
	    'r': 0,
	    'b': 0,
	    't': 0}})

      
def run():
    load()
    
    


