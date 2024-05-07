#!/usr/bin/python3
""" importing the relevant modules"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    auth = (username, token)
    res = requests.get('https://api.github.com/user',
                       auth=auth)
    user_data = res.json()
    id = user_data.get('id')
    print(id)
