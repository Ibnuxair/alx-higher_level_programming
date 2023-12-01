#!/usr/bin/python3
"""
Fetches the value of X-Request-Id variable from the header of a URL response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        req_id = response.getheader('X-Request-Id')
        print(req_id)
