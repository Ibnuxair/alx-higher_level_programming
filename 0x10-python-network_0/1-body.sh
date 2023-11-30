#!/bin/bash
# Sends a GET request to the URL, displays the body of the response if the status code is 200
curl -s -w "%{http_code}" -o response.txt "$1" && [[ $(tail -n1 response.txt) == "200" ]] && curl -s -X GET "$1"
