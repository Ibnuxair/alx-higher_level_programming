#!/usr/bin/python3
"""Fetches content from a URL using urllib."""

import urllib.request


if __name__ == "__main__":
    """Fetches content from a URL and displays it."""
    url = 'https://alx-intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        bytes_content = response.read()
        utf8_content = bytes_content.decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(bytes_content)}")
    print(f"\t- content: b\'{utf8_content}\'")
    print(f"\t- utf8 content: {utf8_content}")
