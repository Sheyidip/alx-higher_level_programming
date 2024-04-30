#!/usr/bin/python3
""" import necessary modules """

import sys
import requests
#  script that takes in a letter and sends a POST request

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            value = ""
        else:
            value = sys.argv[1]
        data = {'q': value}
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        try:
            data = r.json()
            if not data.get('id') and not data.get('name'):
                print("No result")
            else:
                print("[{}] {}".format(data.get('id'), data.get('name')))
        except ValueError:
            print("Not a valid JSON")
    except Exception as e:
        print(f"{e}")
