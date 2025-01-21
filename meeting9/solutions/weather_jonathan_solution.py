
import requests
from typing import Optional, Tuple
import json


def get_city_coords(api_key: str, city_name: str) -> Optional[Tuple[float, float]]:

    try:
        city_coords_params = {
            "q": city_name,
            "appid": api_key
        }
        city_coords_res = requests.get(
            "http://api.openweathermap.org/geo/1.0/direct",
            city_coords_params
        )

        # Check if request was successful
        city_coords_res.raise_for_status()

        data = city_coords_res.json()


        if not data:
            print(f"No coordinates found for city: {city_name}")
            return None

        return data[0]['lat'], data[0]['lon']

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")
        return None
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Failed to parse API response: {str(e)}")
        return None

def get_weather_for_city(api_key: str, lat: float, lon: float, city_name: str) -> str:
    try:
        weather_req_params = {
            "appid": api_key,
            "lat": str(lat),
            "lon": str(lon),
        }
        weather_res = requests.get("https://api.openweathermap.org/data/2.5/weather", weather_req_params)

        # Check if request was successful
        weather_res.raise_for_status()

        data = weather_res.json()

        if not data:
            return f"No weather available for {city_name}"

        return data["weather"][0]["description"]

    except requests.exceptions.RequestException as e:

        return f"API request failed: {str(e)}"

    except (KeyError, IndexError, json.JSONDecodeError) as e:
        return f"Failed to parse API response: {str(e)}"

if __name__ == "__main__":
    city = input("Enter city: ")
    api_key = "b6dca77dbaca8d1e97715708579551f3"

    coords = get_city_coords(api_key, city)
    if coords:
        lat, lon = coords
        print(get_weather_for_city(api_key,lat, lon,city))
