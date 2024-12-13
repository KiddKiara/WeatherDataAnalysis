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
- **Error Handling:** Added error handling to manage API failures gracefully.
- **Logging:** Integrated logging to track the success and failure of data fetching.
- **Testing:** Includes unit tests to validate data loading, cleaning, and visualization outputs.

## Recent Enhancements
- **Error Handling:** Added error handling to manage cases where API requests fail. Errors are logged and printed to the console without interrupting the entire process.
- **Logging:** Implemented logging to record the status of data fetching for each city in `weather_data.log`.
- **Unit Test Expansion:** Expanded tests to validate data ranges for temperature and humidity, as well as ensure the creation of the summary report.
- **Scatter Plot Enhancements:** Improved the scatter plot by adding city annotations for better visualization.

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

## Project Planning Timeline
This project followed a structured timeline to ensure all milestones were met efficiently:
1. **Week 1: Project Setup**
   - Set up a virtual environment and initialized the project repository.
   - Familiarized with the OpenWeatherMap API and obtained an API key.

2. **Week 2: Data Fetching**
   - Developed the `fetch_weather_data.py` script to retrieve weather data for 10 global cities.
   - Implemented error handling and logging to track API request status.

3. **Week 3: Data Cleaning**
   - Created validation steps to handle missing or invalid data.
   - Stored cleaned data in a CSV file for further analysis.

4. **Week 4: Visualization**
   - Designed multiple visualizations using Matplotlib and Seaborn to explore trends in the data.

5. **Week 5: Testing**
   - Added unit tests to validate data loading, cleaning, and visualization outputs.
   - Expanded tests to ensure data ranges were valid.

6. **Week 6: Documentation and Submission**
   - Finalized the `README.md` file and included all recent enhancements.
   - Submitted the completed project repository.

## How to Run
1. **Clone this repository:**
   ```bash
   git clone https://github.com/KiddKiara/WeatherDataAnalysis.git
   cd WeatherDataAnalysis
