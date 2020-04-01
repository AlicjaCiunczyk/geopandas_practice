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
pop = pd.read_csv('Population.csv', sep=';')
pop.head()

# Merge the two dataframes together
merged = pd.merge(map_df, pop, 'JPT_NAZWA_')