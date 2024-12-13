import unittest
import os
import pandas as pd
class TestWeatherDataVisualizations(unittest.TestCase):
    def test_humidity_bar_chart(self):
        """Test if the humidity bar chart was created"""
        self.assertTrue(os.path.exists("humidity_levels.png"), "Humidity bar chart not found!")

    def test_temperature_line_chart(self):
        """Test if the temperature line chart was created"""
        self.assertTrue(os.path.exists("temperature_trends.png"), "Temperature line chart not found!")

    def test_scatter_plot(self):
        """Test if the scatter plot was created"""
        self.assertTrue(os.path.exists("temp_vs_humidity.png"), "Scatter plot not found!")

    def test_average_temperature_bar_chart(self):
        """Test if the average temperature bar chart was created"""
        self.assertTrue(os.path.exists("avg_temp_by_city.png"), "Average temperature bar chart not found!")

    def test_humidity_pie_chart(self):
        """Test if the humidity pie chart was created"""
        self.assertTrue(os.path.exists("humidity_proportion.png"), "Humidity pie chart not found!")

    def test_summary_report_exists(self):
        """Test if the summary report is created"""
        self.assertTrue(os.path.exists("summary_report.txt"), "Summary report not found!")

    def test_valid_temperature_range(self):
        """Test if all temperatures are within a realistic range"""
        df = pd.read_csv("cleaned_weather_data.csv")
        self.assertTrue((df["Temperature"] >= -50).all() and (df["Temperature"] <= 50).all(), "Temperature out of range!")

    def test_valid_humidity_range(self):
        """Test if all humidity values are within a realistic range"""
        df = pd.read_csv("cleaned_weather_data.csv")
        self.assertTrue((df["Humidity"] >= 0).all() and (df["Humidity"] <= 100).all(), "Humidity out of range!")

if __name__ == "__main__":
    unittest.main()
