from pprint import pprint

import requests

API_KEY = "a0fd03d3b0c43b122f7d6dd519c89fc3"

# Get the city name from the user
city = input("insert city: ")

# Build the URL for the OpenWeatherMap API to get the city coordinates
# geo_url = f"http://api.openweathermap.org/geo/1.0/direct?appid={API_KEY}&q={city}"
geo_url = "http://api.openweathermap.org/geo/1.0/direct"
params = {
    "appid": API_KEY,
    "q": city
}


# Send the request and get the response
geo_response = requests.get(geo_url, params)

geo_response.raise_for_status()

# Convert the response to JSON
geo_data = geo_response.json()

# Get the latitude and longitude from the response
lat = geo_data[0]['lat']
long = geo_data[0]['lon']

# Build the URL for the OpenWeatherMap API to get the weather data
weather_url = f"https://api.openweathermap.org/data/2.5/weather"
params = {
    "appid": API_KEY,
    "lat": lat,
    "lon": long,
    "units": "metric"

}

# Send the request and get the response
weather_response = requests.get(weather_url, params)

# Print the weather data
pprint(weather_response.json())