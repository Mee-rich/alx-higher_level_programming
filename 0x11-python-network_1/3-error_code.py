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
    
    url = sy.argv[1]

    try:
        with request.urlopen(url) as res:
            body = res.read().decode('utf-8')

            print(body)

    except error.HTTPError as e:
        print('Error code:' e.code)
