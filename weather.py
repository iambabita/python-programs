# Weather Data Analysis Program

# Sample weather data for 7 days
# Format: (Day, Temperature in °C, Humidity %, Rainfall in mm)
weather_data = [
    ("Monday", 25, 60, 0),
    ("Tuesday", 28, 65, 5),
    ("Wednesday", 30, 70, 0),
    ("Thursday", 27, 68, 12),
    ("Friday", 26, 62, 0),
    ("Saturday", 29, 75, 20),
    ("Sunday", 31, 80, 0)
]

total_temp = 0
total_rain = 0
rainy_days = 0

max_temp = weather_data[0][1]
min_temp = weather_data[0][1]

# Analyze data
for day, temp, humidity, rain in weather_data:
    total_temp += temp
    total_rain += rain

    if rain > 0:
        rainy_days += 1

    if temp > max_temp:
        max_temp = temp
    if temp < min_temp:
        min_temp = temp

average_temp = total_temp / len(weather_data)


print("Weather Data Analysis")
print("---------------------")
print(f"Average Temperature: {average_temp:.2f} °C")
print(f"Maximum Temperature: {max_temp} °C")
print(f"Minimum Temperature: {min_temp} °C")
print(f"Total Rainfall: {total_rain} mm")
print(f"Number of Rainy Days: {rainy_days}")
