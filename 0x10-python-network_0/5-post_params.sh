#!/bin/bash
# Takes in a URL, sends a POST request with variables, and displays the body of the response
echo -n $(curl -s -X POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1")
