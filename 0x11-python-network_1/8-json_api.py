#!/usr/bin/python3
'''
Takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]

        url = 'http://0.0.0.0:5000/search_user'

        r = requests.post(url, data={'q': q})

        try:
            json_response = r.json()
            print("[{}] {}".format(json_response['id'], json_response['name']))
        except Exception:
            print('Not a valid JSON')

    elif len(sys.argv) == 1:
        print('No result')
