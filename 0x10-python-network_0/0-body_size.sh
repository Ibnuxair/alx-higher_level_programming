#!/bin/bash
# This script fetches the size of the body in bytes from a given URL using curl
curl -s -w "%{size_download}" -o /dev/null "$1"
