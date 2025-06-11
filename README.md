# 🌍 Global Earthquake Mapping & Analysis

This project analyzes and visualizes global earthquake data using **Python**, **Plotly**, and geospatial datasets.  
It highlights core skills in **data parsing**, **cleaning**, and **interactive visualization**, making it ideal for data analyst portfolios and real-world data work.

---

## 🧠 Project Overview

- Parses and analyzes global earthquake data from **GeoJSON** and **CSV** sources.
- Creates interactive maps that visualize earthquake **magnitude**, **location**, and **frequency**.
- Optionally includes **global fire data mapping** using NASA satellite inputs.
- Emphasizes automation, scalability, and real-world geospatial insight.

---

## 🔍 Skills Demonstrated

- **Data Wrangling**: Extracted and cleaned structured data from GeoJSON and CSV formats.
- **Geospatial Visualization**: Used Plotly to create dynamic global maps and scatter plots.
- **Automation & Optimization**: Refactored scripts for reusability and modularity.

---

## ✨ Key Features

- 🌐 **Global Earthquake Mapping**:
  - Plots recent earthquakes on a world map, scaled by magnitude.
  - Focus on events from the **past 30 days** using real data from the **USGS**.

- 🔥 **Optional Fire Mapping**:
  - Visualizes active global fire locations using NASA’s MODIS satellite data.

- 📍 **Interactive Plots**:
  - Hoverable tooltips showing magnitude, location, and depth.
  - Fully interactive zoom and pan experience via Plotly.

---

## 🛠️ Technologies Used

| Tool       | Purpose                                |
|------------|----------------------------------------|
| Python     | Main scripting and data handling       |
| Plotly     | Interactive map and scatter plots      |
| Pandas     | Data manipulation and filtering        |
| GeoJSON    | Earthquake data format (from USGS)     |
| CSV        | Used for alternate or fire datasets    |

---

## 📈 Future Improvements

- 🔄 **Real-Time Data**: Automate refresh from USGS/NASA APIs.
- 📊 **Historical Analysis**: Time-series analysis of global seismic activity.
- 🖥️ **Dashboard UI**: Build a web-based dashboard for public exploration.

---

## 🌍 Data Sources

- **USGS Earthquake Catalog**:  
  [https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)

- **NASA MODIS Fire Data**:  
  [https://firms.modaps.eosdis.nasa.gov/](https://firms.modaps.eosdis.nasa.gov/)

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/prabhdev-khanijaon/global-earthquake-mapping-analysis.git
cd global-earthquake-mapping-analysis
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Visualizations

#### 📌 Earthquake Map (last 30 days)

```bash
python eq_explore_data.py
```

#### 🔥 Fire Mapping (optional)

```bash
python world_fires.py
```

> Visualizations will open in your browser via Plotly as **interactive maps**.

---

## 📌 Notes

* Built with **Python 3.x**
* Ideal for showcasing geospatial analysis and interactive visualizations
* Demonstrates end-to-end pipeline: **data ingestion → processing → visual storytelling**

---

Feel free to fork, star ⭐, or contribute!
