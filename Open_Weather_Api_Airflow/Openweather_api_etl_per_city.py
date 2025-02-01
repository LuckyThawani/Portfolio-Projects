import json
from datetime import datetime
import pandas as pd
import requests

# Define the city for which weather data is required
city_name = "Jaipur"
# Base URL for OpenWeather API
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

# Read API key from credentials file
with open("credentials.txt", 'r') as f:
    api_key = f.read().strip()  # Ensure no extra spaces or newline characters

# Construct the full API request URL
full_url = base_url + city_name + "&APPID=" + api_key

# Function to convert temperature from Kelvin to Celsius
def kelvin_to_celsius(temp_in_kelvin):
    temp_in_celsius = temp_in_kelvin - 273.15
    return temp_in_celsius

# Function to extract, transform, and load (ETL) weather data
def etl_weather_data(url):
    # Send an HTTP GET request to fetch weather data
    r = requests.get(url)
    data = r.json()  # Parse JSON response
    
    # Extract relevant weather details from the response
    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_celsius = kelvin_to_celsius(data["main"]["temp"])
    feels_like_celsius = kelvin_to_celsius(data["main"]["feels_like"])
    min_temp_celsius = kelvin_to_celsius(data["main"]["temp_min"])
    max_temp_celsius = kelvin_to_celsius(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Convert timestamps to human-readable datetime format
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

    # Transform extracted data into a structured format
    transformed_data = {
        "City": city,
        "Description": weather_description,
        "Temperature (C)": round(temp_celsius, 1),
        "Feels Like (C)": round(feels_like_celsius, 1),
        "Minimum Temp (C)": round(min_temp_celsius, 1),
        "Maximum Temp (C)": round(max_temp_celsius, 1),
        "Pressure": pressure,
        "Humidity": humidity,
        "Wind Speed": wind_speed,
        "Time of Record": time_of_record,
        "Sunrise (Local Time)": sunrise_time,
        "Sunset (Local Time)": sunset_time                        
    }

    # Convert the dictionary into a DataFrame for structured storage
    df_data = pd.DataFrame([transformed_data])
    
    # Save the data to a CSV file
    df_data.to_csv("current_weather_data_jaipur.csv", index=False)
    print("Weather data saved to current_weather_data_jaipur.csv")

# Main entry point of the script
if __name__ == '__main__':
    etl_weather_data(full_url)
