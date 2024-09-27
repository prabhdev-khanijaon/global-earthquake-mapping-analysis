from pathlib import Path
import csv

import plotly.express as px

# Read data as a string and convert to a python object.
path = Path('fires_data/MODIS_C6_1_Global_7d.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

# Find out which column data, indexes we need.
for index, column_header in enumerate(header_row) :
    print(index, column_header)
# We want: 0 latitude, 1 longitude, 2 brightness, 5 acq_date.

# Extract latitude, longitude, brightness, dates.
lats, lons, bris, dates = [], [], [], []
for row in reader :
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    bris.append(float(row[2]))
    dates.append((row[5]))

# Check the list results.
print(lats[:5])
print(lons[:5])
print(bris[:5])
print(dates[:5])

# Visualize the results.
title = 'World Fires Recorded by MODIS From 17 July 2024 to 26 July 2024'
fig = px.scatter_geo(lat=lats, lon=lons, size=bris, title=title,
                     color=bris,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Brightness'},
                     projection='natural earth',
                     )

fig.show()