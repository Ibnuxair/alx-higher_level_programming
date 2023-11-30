#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me causing the server to respond with a specific message
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
