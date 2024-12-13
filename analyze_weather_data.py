import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("weather_data.csv")

# Display basic information about the data
print("Basic Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Example cleaning step: Ensure temperature values are numeric
df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")

# Drop rows with missing Temperature or Humidity
df = df.dropna(subset=["Temperature", "Humidity"])

# Display cleaned data
print("\nCleaned Data:")
print(df.head())

# Save cleaned data
df.to_csv("cleaned_weather_data.csv", index=False)
print("\nCleaned data saved to cleaned_weather_data.csv")

# Bar chart: Humidity levels by city
sns.barplot(x="City", y="Humidity", data=df)
plt.title("Humidity Levels by City")
plt.xticks(rotation=45)
plt.savefig("humidity_levels.png")
plt.show()

# Line plot: Temperature trends by city
sns.lineplot(x="City", y="Temperature", data=df, marker="o")
plt.title("Temperature Trends by City")
plt.xticks(rotation=45)
plt.savefig("temperature_trends.png")
plt.show()

# Scatter plot: Temperature vs. Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Temperature", y="Humidity", hue="City", data=df)
plt.title("Temperature vs. Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("temp_vs_humidity.png")
plt.show()

# Bar chart: Average temperature by city
plt.figure(figsize=(10, 6))
avg_temp = df.groupby("City")["Temperature"].mean()
avg_temp.plot(kind="bar", color="skyblue")
plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.savefig("avg_temp_by_city.png")
plt.show()

# Pie chart: Proportion of humidity by city
plt.figure(figsize=(8, 8))
total_humidity = df.groupby("City")["Humidity"].sum()
total_humidity.plot(kind="pie", autopct="%1.1f%%", startangle=90, colormap="viridis")
plt.title("Proportion of Humidity by City")
plt.ylabel("")  # Hide y-axis label for better appearance
plt.savefig("humidity_proportion.png")
plt.show()
