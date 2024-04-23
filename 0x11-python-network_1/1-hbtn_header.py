#!/usr/bin/python3
""" importing the urllib and sys packages"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        variable = 'X-Request-Id'
        if variable in headers:
            value = headers[variable]
            print('{}'.format(value))
