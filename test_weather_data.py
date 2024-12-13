import unittest
import os

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

if __name__ == "__main__":
    unittest.main()
