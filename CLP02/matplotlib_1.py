import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
data = pd.read_csv('data/first_week_weather.csv')

# Step 2: Convert Date_Time to datetime type
data['Date_Time'] = pd.to_datetime(data['Date_Time'])

# Step 3: Extract just the date part and group by date
daily_temps = data.groupby(data['Date_Time'].dt.date)['Temperature_C'].mean().reset_index()

# Step 4: Sort by date and get the first week of data
daily_temps = daily_temps.sort_values('Date_Time').head(7)

# Step 5: Plot the data
plt.figure(figsize=(10, 5))
plt.plot(daily_temps['Date_Time'], daily_temps['Temperature_C'], 
         marker='o', linestyle='-', color='b', linewidth=2, markersize=8)

plt.title('Average Daily Temperature Variations Over a Week')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
