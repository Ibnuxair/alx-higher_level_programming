#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value of the

X-Request-Id variable from the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    req_id = response.headers.get('X-Request-Id')
    print(req_id)
