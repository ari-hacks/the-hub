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
"""
Need a function to parse each graph 
"""
def load():
    document.getElementById('load-python').classList.add('alert-success')
    document.getElementById('load-python').innerHTML = 'Python Loaded'

# def get_data():
#     rawdata = 'name,age\nDan,33\nBob,19\nSheri,42'
#     myreader = csv.reader(file_data.splitlines())
#     for row in myreader:
#         print(row[0], row[1])

def process_upload():
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
    print(df.num_pets)
    df.plot(kind='bar',x='num_children',y='num_pets',color='red')
    #df.iplot(kind='bar',x='num_children',y='num_pets',color='red')
    #document.getElementById('plot1').src = df
    # Plotly.plot(document.getElementById('plot1'),
    #          [{ 'y': df.num_pets, 'x': df.num_children }],
    #           {
    #      'title': 'Title of the Graph',
    #       'xaxis': {
    #          'title': 'x-axis title'
    #          },
    #      'yaxis': {
    #          'title': 'y-axis title'
    #       }
    #      }
    #          )
    
    fig,ax = plt.subplots()
    ax.plot(df.num_children,df.num_pets)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_str = 'data:image/png;base64,' + base64.b64encode(buf.read()).decode('UTF-8')
          
    document.getElementById("pyplotfigure").src=img_str


def run():
    load()
    
    


