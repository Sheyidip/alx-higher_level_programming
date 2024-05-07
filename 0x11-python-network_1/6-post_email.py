#!/usr/bin/python3
"""importing the sys and requests module"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.post(url, data={'email': sys.argv[2]})
    print(f'{r.text}')
