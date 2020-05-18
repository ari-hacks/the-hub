from js import document, Plotly,console
import logging
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv
import sys
import matplotlib.pyplot as plt
import io, base64


logging.basicConfig(level=logging.INFO)

def load():
    document.getElementById('load-python').classList.add('alert-success')
    document.getElementById('load-python').innerHTML = 'Python Loaded'

def process_scatter():
    print('executed scatter plot')
    
def process_pie():
    print('executed pie plot')

    
def process_time_series():
    print('executed time plot')

def process_relationship_map():
     print('executed relationship plot')


def process_geo_maps():
    print('executed geo plot')

    
def process_3d_maps():
     print('executed 3d plot')

    
    
def process_upload():
    #based on button id call correct method of plotting
    rows = []
    file_data = document.getElementById("output").textContent
    console.log(file_data)  
    csv_reader = csv.reader(file_data.splitlines())
    for row in csv_reader:
        print(row)
        rows.append(row)
        
    df = pd.DataFrame(data=rows)
    set_header = df.iloc[0] 
    df = df[1:] 
    df.columns = set_header
    #df=df.astype(float)
    #need logic to check if any values are words and if not convert to numbers 
    df.num_children=pd.to_numeric(df.num_children)
    df.num_pets=pd.to_numeric(df.num_pets)
    print(df)
    pets = df[df.columns[5]].values
    children = df[df.columns[4]].values
    print(children)
    
    Plotly.plot(document.getElementById('plot1'),
            [{'x':children, 'y':[20,2,3,2],
            'labels': ['t1','t2'],
            'type': 'pie',
            'name': 'Starry Night',
            'hoverinfo': 'label+percent+name',
            'textinfo': 'none'}],
              {
         'title': 'Title of the Graph',
          'xaxis': {
             'title': df[df.columns[4]].name,
             'label' : 'children'
             },
         'yaxis': {
             'title': df[df.columns[5]].name
          }
         }
             )
    # Plotly.newPlot(document.getElementById('plot1'),
    # data = [{'x':[1, 2, 3, 4, 5], 'y':[10, 20, 30, 20, 10], 'type':'scatter',
    #          'mode':'markers', 'marker':{'size':20}
    #         }],
    # layout = {'hovermode':'closest',
    #           'title':'Click on Points'
    #  })
    
    # fig,ax = plt.subplots()
    # ax.plot(df.num_children,df.num_pets)
    # buf = io.BytesIO()
    # fig.savefig(buf, format='png')
    # buf.seek(0)
    # img_str = 'data:image/png;base64,' + base64.b64encode(buf.read()).decode('UTF-8')
          
def run():
    load()
    
    


