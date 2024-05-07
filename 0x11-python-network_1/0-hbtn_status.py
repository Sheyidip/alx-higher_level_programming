#!/usr/bin/python3
""" importing python urllib library"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content_bytes = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(content_bytes)))
        print('\t- content: {}'.format(content_bytes))
        print('\t- utf8 content: {}'.format(content_bytes.decode('utf-8')))
