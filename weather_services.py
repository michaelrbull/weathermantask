import sys
import requests
from flask import Flask, json, jsonify

# This function closes the program using the exit function from the sys module.

def program_close():
    sys.exit

# This function pulls the JSON data from the weather API. Which then calls the weather_check
# function later in the program. Also included is a try/except block incase the user experiences
# a connection error. 

def get_weather():
    try:
        weather_response = requests.get("http://localhost:5001/")
        weather_data = json.loads(weather_response.text)
        return weather_check(weather_data)    
    except requests.exceptions.ConnectionError:
        print('No Internet Connection, please try again later.')
        program_close()

# Creates variable for the following weather_check function to use.

sunny_cities = []

# This function checks the weather data from the API JSON pull and specifically takes only
# the cities which are sunny and add them into a list defined as sunny_cities

def weather_check(weather_data):
    for weather in weather_data:
        test_weather = (weather['weather'])
        if test_weather == "sunny":
            sunny_cities.append(weather["location"])   
    return(sunny_cities)
    
# Calls the get_weather function which in return also cals the weather_check function.

get_weather()