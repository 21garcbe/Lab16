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

#set path to csv of fire data
path = Path('world_fires_1_day.csv')

lats = []
lons = []
brightnesses = []
dates = []
hover_texts = []

#read csv
with path.open() as file:
    reader = csv.reader(file)
    header_row = next(reader)
    
    for index, row in enumerate(reader):
        if index >= 1000:
            break

        try:

            lat = float(row[0])
            lon = float(row[1])
            brightness = float(row[2])
            date = row[5]
        except ValueError:
            print(f"Skipped invalid data on row {index+1}")
        
        else:

            lats.append(lat)
            lons.append(lon)
            brightnesses.append(brightness)
            dates.append(date)
            hover_texts.append(f"Coordinates: ({lat}, {lon})<br>Date: {date}")

        
#set title and figure to a basic worldmap
title = "Global Fires"
fig = ex.scatter_geo(lat= lats, lon = lons, color = brightnesses, title = title, hover_name= hover_texts, labels= {"color": "Brightness"})
fig.show()
fig.write_html("Global_Fires.html")


