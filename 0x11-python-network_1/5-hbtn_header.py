#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL

"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
