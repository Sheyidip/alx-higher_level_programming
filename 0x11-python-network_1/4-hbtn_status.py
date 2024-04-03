#!/usr/bin/python3
""" importing the request module"""

import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    output = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(output)))
    print('\t- content: {}'.format(output))
