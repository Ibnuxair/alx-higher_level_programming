#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the body

of the response (decoded in utf-8).
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            bytes_content = response.read()
            utf8_content = bytes_content.decode('utf-8')
            print(utf8_content)
    except urllib.request.HTTPError as e:
        print(f"Error code: {e.code}")
