#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -s -w "%{http_code}" -o response.txt "$1" | grep -q 200 && cat response.txt
