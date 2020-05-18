from js import document, Plotly,console
import logging
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import csv


logging.basicConfig(level=logging.INFO)

def load():
    document.getElementById('load-python').classList.add('alert-success')
    document.getElementById('load-python').innerHTML = 'Python Loaded'


def process_upload():
    file_data = document.getElementById("output").textContent
    console.log(file_data)  
    data_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
    with open('/tmp.csv', 'w', newline='') as file:
        console.log(file)
        console.log(data_list)
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data_list)
        console.log(writer)
    # pds = pd.re(file_data)
    # console.log(pds) 
    """
    Test Plot
    """
    # x = np.linspace(0, 2.0 * np.pi, 100)
    # y = np.sin(x)
    
    # Plotly.plot(document.getElementById('plot1'),
    #         [{ 'y': y, 'x': x }],
    #          {
    #     'title': 'Title of the Graph',
    #      'xaxis': {
    #         'title': 'x-axis title'
    #         },
    #     'yaxis': {
    #         'title': 'y-axis title'
    #      }
    #     })
    """
    Relationship Map Plot
    """
    
       

    
def run():
    load()
    
    
# d1 = {'row1': [1,2,3,4], 'row2': [2,3,32,2], 'row3': [4,3,2,2], 'row4': [4,3,2,2]}
# d2 = {
# '1,2,3,4'
# '2,3,32,2'
# '4,3,2,2'
# '4,3,2,2'}
# df = pd.DataFrame(d1)

# df = pd.DataFrame(d2)
# print('DataFrame:\n', df)

# # default CSV
# csv_data = df.to_csv()
# print('\nCSV String:\n', csv_data)


