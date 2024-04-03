#!/usr/bin/python3
""" importing the urllib and sys packages"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'email': sys.argv[2]}
    headers = {'User_Agent': user_agent}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
        output = response.read()
        response_str = output.decode('utf-8')
        print(response_str)
