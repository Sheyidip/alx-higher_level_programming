#!/usr/bin/python3
""" Importing the requests module """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    response_headers = r.headers
    for header, value in response_headers.items():
        if header == 'X-Request-Id':
            print(f'{value}')
