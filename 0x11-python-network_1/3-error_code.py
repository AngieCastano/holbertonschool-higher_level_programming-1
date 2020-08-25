#!/usr/bin/python3
'''
Takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
'''
import urllib.request as request
import urllib
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
