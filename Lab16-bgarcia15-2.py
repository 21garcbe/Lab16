"""
Lab 16 Option 2:
Map global Fire Data
A program that reads the world_fires_1_day.csv file
and plots the fire data on an interactive world map using plotly

Author: Ben Garcia
"""

import plotly.express as ex
import csv
from pathlib import Path 


"""Plots gobal fire data from csv format using plotly"""
#set path to csv of fire data
path = Path('world_fires_1_day.csv')


lats = []
lons = []

#read csv
with path.open() as file:
    reader = csv.reader(file)
    row = next(reader)
    
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])

        lats.append(lat)
        lons.append(lon)

        
#set title and figure to a basic worldmap
title = "Global Fires"
fig = ex.scatter_geo(lat = lats, lon= lons, title = title)
fig.show()


