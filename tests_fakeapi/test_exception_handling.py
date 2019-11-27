# Imports requests, pytest, mock, patch and the function to be mocked 
# from the weather services folder (get_weather)

import requests
import pytest
import mock
from mock import patch
import sys

# Use the path function from the system module, this allows this program to import files from one directory up.
sys.path.append('../')

#This imports the function get_weather, from which the requests.get call is to be mocked.

from weather_services import get_weather

# Using mock patch, I am making a mocked version of the requests.get function
# and patching it to return a connection error.
# Then using 'with' I am asserting that pytest checks that a connection error is run 
# when the get_weather function is run.

@mock.patch('weather_services.requests.get')
def test_mock_response(mock_get):
    mock_get.side_effect = ConnectionError 
    with pytest.raises(ConnectionError):
        get_weather()   

# This runs the mocked function defined prior.

test_mock_response()