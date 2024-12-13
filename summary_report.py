import pandas as pd

# Load cleaned data
df = pd.read_csv("cleaned_weather_data.csv")

# Calculate key statistics
avg_temp = df["Temperature"].mean()
avg_humidity = df["Humidity"].mean()
hottest_city = df.loc[df["Temperature"].idxmax(), "City"]
most_humid_city = df.loc[df["Humidity"].idxmax(), "City"]

# Generate the report
with open("summary_report.txt", "w") as file:
    file.write("Weather Data Summary Report\n")
    file.write("===========================\n")
    file.write(f"Average Temperature: {avg_temp:.2f}°C\n")
    file.write(f"Average Humidity: {avg_humidity:.2f}%\n")
    file.write(f"Hottest City: {hottest_city}\n")
    file.write(f"Most Humid City: {most_humid_city}\n")

print("Summary report generated: summary_report.txt")
