#!/usr/bin/python3
"""
This script:
    - takes in a URL
    - sends a request to the URL
    - displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:' e.code)
