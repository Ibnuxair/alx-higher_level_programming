#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request, and

displays the body of the response (decoded in utf-8).
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = 'email=' + email
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        bytes_content = response.read()
        utf8_content = bytes_content.decode('utf-8')

        print(f"Your email is: {utf8_content}")
