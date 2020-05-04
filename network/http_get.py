#!/usr/bin/env python3
"""
    Perform HTTP GET request for a website with Python
    Author: Miguel Rentes
    https://github.com/rentes/python3-code-snippets/blob/master/network/http_get.py
    Python version: 3.7.2
    This simple script expects one argument: the website URL
"""
import requests
from requests.exceptions import HTTPError
import sys

response = requests.get(sys.argv[1])
try:
    # Let's check the status code for our request
    response.raise_for_status()
except HTTPError as http_error_exception:
    print(f'HTTP error occurred: {http_error_exception}')
except Exception as other_error_exception:
    print(f'Other error occurred: {other_error_exception}')
else:
    print('Success GETting the website! The website content is: ')
    print(response.content)