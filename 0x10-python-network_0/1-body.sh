#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
echo -n $(curl -s -X GET "$1")
