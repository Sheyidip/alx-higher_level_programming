#!/usr/bin/python3
""" importing urllib and sys modules"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            output = response.read()
            body = output.decode('utf-8')
            print(f'{body}')
    except HTTPError as e:
        print("Error code: {}".format(e.code))
