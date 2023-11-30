#!/bin/bash
# Sends a JSON POST request with file contents to a URL passed as the first argument and displays the response body
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"