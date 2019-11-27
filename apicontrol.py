import sys
import requests
from flask import Flask, json, jsonify

if len(sys.argv) > 1:

# If argument to program contains the string "weather", run API containing
# the weather fixtures and use target port specified in weather_fixtures file.
    
    if sys.argv[1] == "weather": 
        from weather_fixtures import weather_fixture 
        from weather_fixtures import target_port

        api = Flask(__name__)

        @api.route('/', methods=['GET'])
        def get_payload():
            return jsonify(weather_fixture)

# If argument to program contains the string "flight", run API containing
# the flight fixtures and use target port specified in flight_fixtures file.

    elif len(sys.argv) > 1:
        if sys.argv[1] == "flights":
            from flight_fixtures import flightnum_madrid
            from flight_fixtures import flightnum_berlin
            from flight_fixtures import flightnum_london
            from flight_fixtures import flightnum_prague
            from flight_fixtures import flightnum_baku
            from flight_fixtures import flightnum_moscow
            from flight_fixtures import target_port
           
            api = Flask(__name__)

# Each flight fixture has its own individual route on the API which is defined here.
# The exact variable from each route is called too.

            @api.route("/")
            def index():
                return 'Index Page'

            @api.route("/madrid")
            def weathermadrid():
                return flightnum_madrid

            @api.route("/berlin")
            def weatherberlin():
                return flightnum_berlin

            @api.route("/london")
            def weatherlondon():
                return flightnum_london  

            @api.route("/prague")      
            def weatherprague():
                return flightnum_prague

            @api.route("/baku")
            def weatherbaku():
                return flightnum_baku   

            @api.route("/moscow")
            def weathermoscow():
                return flightnum_moscow

# Unsure on __name__ and __main section,
# but second line specifies the host and ports.

if __name__ == "__main__":
    api.run(host = "localhost", port = target_port)