"""
Lab 16 Option 2:
Map global Fire Data
A program that reads the world_fires_1_day.csv file
and plots the fire data on an interactive world map using plotly

Author: Ben Garcia
"""

import plotly.express as ex
from pathlib import Path 

class Main():
    """Plots gobal fire data from csv format using plotly"""
    #set path to csv of fire data
    path = Path('world_fires_1_day.csv')
    #set title and figure to a basic worldmap
    title = "Global Fires"
    fig = ex.scatter_geo(lat = lats, lon= lons, title = title)

