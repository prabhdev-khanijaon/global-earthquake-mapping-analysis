# Global Earthquake Mapping & Analysis

## Overview
This project is focused on analyzing and visualizing global earthquake data using Python. The primary goal is to showcase data analysis and visualization skills relevant to data analyst roles. The project includes scripts that parse, clean, and analyze earthquake data, as well as generate interactive visualizations using Plotly.

## The project demonstrates the following core competencies:
Data Parsing: Reading and processing raw data from geoJSON and CSV files.
Data Cleaning: Extracting relevant data (latitude, longitude, magnitude) and handling missing or incomplete information.
Data Visualization: Presenting insights via interactive maps that allow users to explore earthquake magnitudes and locations around the world.

## Skills Demonstrated
Data Wrangling: Extracting and cleaning data from various sources (geoJSON, CSV).
Geospatial Visualization: Using Plotly for interactive and insightful data visualizations on global maps.
Automation & Optimization: Refactoring code for improved automation and scalability.

## Key Features
Global Earthquake Mapping: Interactive visualizations of earthquake occurrences worldwide, scaled by magnitude.
Recent Earthquake Analysis: Focus on seismic events from the past 30 days.
Fire Event Mapping (Optional): Visual representation of recent global fires using satellite data for added insight into natural disaster patterns.

## Technologies Used
Python: Primary language for data processing and visualization.
Plotly: For creating interactive maps and scatter plots.
Pandas: For data manipulation and cleaning.
GeoJSON & CSV: Earthquake and fire data formats used for analysis.

## Future Improvements
Real-time Data Integration: Automating the update of earthquake and fire data using live API connections.
Extended Analysis: Incorporating additional features like time-based filtering and the analysis of historical trends in seismic activity.
Dashboard Integration: Expanding the project to include a user-friendly dashboard for non-technical users.

## Data Sources
Earthquake Data: The earthquake data is sourced from USGS Earthquake Catalog, providing real-time earthquake information.
Fire Data: Fire data is sourced from NASA’s MODIS Fire Database, offering satellite-based fire detections.

## How to Run the Project
Clone the repository:

bash
Copy code
git clone https://github.com/prabhdev-khanijaon/global-earthquake-mapping-analysis.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run any of the Python scripts to visualize the earthquake or fire data. For example:

bash
Copy code
python eq_explore_data.py
For fire mapping, use:

bash
Copy code
python world_fires.py

