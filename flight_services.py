
# Imports requests library, json and jsonify and sunny_cities list.

import requests
from flask import Flask, json, jsonify
from weather_services import sunny_cities

# This function uses the cities from the sunny_cities list.
# Using a for loop, only the cities requested have their specific flight URL pulled through.

sunny_flight_num = []

def weather_flight_match():
    for city in sunny_cities:
        flight_response = requests.get("http://localhost:5002/" + city.lower())
        flight_info = json.loads(flight_response.text)
        for flight in flight_info:
            sunny_flight_num.append(flight["flight"])
    return(sunny_flight_num)

# Calls the weather_flight_match function defined prior.

weather_flight_match()