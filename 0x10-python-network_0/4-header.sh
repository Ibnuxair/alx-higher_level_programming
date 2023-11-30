#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of the response with a custom header
echo -n $(curl -s -H "X-School-User-Id: 98" -X GET "$1")
