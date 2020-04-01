#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Reading the shp data
map_df = gpd.read_file('Wojewodztwa\\Wojewodztwa.shp')
map_df.head()

# Changing the names of the Voivodeships (there's probably a better way to do it)
map_df['JPT_NAZWA_'] = ['Śląskie', 'Opolskie', 'Wielkopolskie', 'Zachodniopomorskie', 'Świętokrzyskie', 'Kujawsko-pomorskie',
                        'Podlaskie', 'Dolnośląskie', 'Podkarpackie', 'Małopolskie', 'Pomorskie', 'Warmińsko-mazurskie',
                        'Łódzkie', 'Mazowieckie', 'Lubelskie', 'Lubuskie']
# Plot the basic map
map_df.plot()

# Import the csv file with the population data
pop = pd.read_csv("Population.csv", sep=";")
pop.head()

# Merge the two dataframes together
merged = pd.merge(map_df, pop, on = "JPT_NAZWA_")
# Create density column
merged["Density"] = merged["Population"]/merged["Area"]

### POPULATION PER VOIVODESHIP ###
# create figure and axes for Matplotlib
fig, ax = plt.subplots(figsize = (16, 12))
merged["rep"] = merged["geometry"].centroid
map_points = merged.copy()
# Plot the heatmap of population
map_points.plot(column = merged["Population"], cmap = "Greens", linewidth = 1.2,
                ax = ax, edgecolor = "0.7", legend=True, 
                legend_kwds={'label': "Population by Voivodeship", 
                             'orientation': "horizontal"})
map_points.set_geometry("rep", inplace = True)

# Add Voivodeship names
for i in range(len(merged["rep"])):
    x = merged["rep"][i].bounds[0]
    y = merged["rep"][i].bounds[1]
    label = merged["JPT_NAZWA_"][i]
    ax.text(x, y, label, fontsize = 10)

### POPULATION DENSITY PER VOIVODESHIP ###
# create figure and axes for Matplotlib
fig1, ax1 = plt.subplots(figsize = (16, 12))
map_points = merged.copy()
# Plot the heatmap of population density
map_points.plot(column = merged["Density"], cmap = "Reds", linewidth = 1.2, ax = ax1,
                edgecolor = "0.7", legend=True, 
                legend_kwds={'label': "Population density by Voivodeship", 
                             'orientation': "horizontal"})
map_points.set_geometry("rep", inplace = True)

# Add Voivodeship names
for i in range(len(merged["rep"])):
    x = merged["rep"][i].bounds[0]
    y = merged["rep"][i].bounds[1]
    label = merged["JPT_NAZWA_"][i]
    ax1.text(x, y, label, fontsize = 10)

