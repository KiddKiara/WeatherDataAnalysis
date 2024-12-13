# Analysis of Global Weather Patterns

## Overview
This project analyzes weather patterns for 10 global cities using the OpenWeatherMap API. The data is fetched, cleaned, and visualized to explore trends in temperature and humidity. Additional visualizations provide deeper insights into weather patterns across the selected cities.

## Features
- **Data Loading:** Weather data is fetched for 10 cities using the OpenWeatherMap API and saved in CSV format.
- **Data Cleaning:** The data is cleaned using pandas, including handling missing values and ensuring correct data types.
- **Visualizations:** Multiple visualizations are created using Matplotlib and Seaborn to illustrate weather trends:
  - Humidity levels by city (Bar Chart).
  - Temperature trends by city (Line Chart).
  - Relationship between temperature and humidity (Scatter Plot).
  - Average temperature by city (Bar Chart).
  - Proportion of humidity by city (Pie Chart).
- **Testing:** Includes unit tests to validate data loading, cleaning, and visualization outputs.

## Visualizations
The following visualizations are generated:
1. **Humidity Levels by City (Bar Chart):**
   - Displays humidity levels for each city.
2. **Temperature Trends by City (Line Chart):**
   - Illustrates temperature variations across cities.
3. **Temperature vs. Humidity (Scatter Plot):**
   - Explores the relationship between temperature and humidity for each city.
4. **Average Temperature by City (Bar Chart):**
   - Highlights the average temperature for each city.
5. **Proportion of Humidity by City (Pie Chart):**
   - Visualizes the proportion of total humidity contributed by each city.

## How to Run
1. **Clone this repository:**
   ```bash
   git clone https://github.com/KiddKiara/WeatherDataAnalysis.git
   cd WeatherDataAnalysis
