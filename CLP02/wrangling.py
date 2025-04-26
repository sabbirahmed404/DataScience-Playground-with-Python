import pandas as pd

# Read the original CSV file
data = pd.read_csv('data/weather_data.csv')

# Convert Date_Time to datetime
data['Date_Time'] = pd.to_datetime(data['Date_Time'])

# Filter data for the first week of the year (January 1-7)
first_week = data[
    (data['Date_Time'].dt.year == 2024) & 
    (data['Date_Time'].dt.month == 1) & 
    (data['Date_Time'].dt.day <= 7)
]

# Sort by date and time
first_week = first_week.sort_values('Date_Time')

# Save the filtered data to a new CSV file
first_week.to_csv('data/first_week_weather.csv', index=False)

print(f"Saved {len(first_week)} records from the first week of 2024")
