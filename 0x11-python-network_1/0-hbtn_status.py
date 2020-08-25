#!/usr/bin/python3
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        r = response.read()
        print('Body response:')
        print('\t- type:', type(r))
        print('\t- content:', r)
        print('\t- utf8 content:', r.decode('utf-8'))
