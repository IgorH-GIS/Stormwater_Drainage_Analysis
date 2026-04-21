# QGIS Hydrology Exporter: Stormwater Drainage Networks

**Author:** Igor Hajducki | DroneCube Analytics
**Tech Stack:** Python, PyQGIS, QGIS 3.x, DEM (Digital Elevation Models)

## Overview
This Python script automates the extraction of hydrological vector geometries (flow accumulation lines, drainage channels) from QGIS into a structured `.csv` format. It is designed to assist Civil Engineers and Real Estate Developers in **Stormwater Management** and **Flood Risk Assessment** prior to construction.

## Features
* **Automated Length Calculation:** Extracts the exact length (in meters) of drainage channels directly from DEM-derived vector layers.
* **Risk Categorization:** Automatically flags channels based on length/runoff potential for quicker engineering review.
* **Engineering-Ready Output:** Generates a structured CSV file that seamlessly integrates with civil engineering planning tools and cost-estimation spreadsheets.

## Usage
1. Generate flow accumulation/drainage lines from a drone-captured DEM.
2. Select the active drainage vector layer in the QGIS environment.
3. Run the script within the QGIS Python Console.
4. A `Drainage_Network_Report.csv` is automatically saved to the active directory, turning visual topographic data into actionable numbers.
