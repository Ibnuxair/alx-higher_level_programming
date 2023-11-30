#!/bin/bash
# Sends a request to a URL passed as an argument and displays only the status code of the response
echo -n $(curl -s -I -w "%{http_code}" -o /dev/null "$1")
