#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
if curl -s -L -X DELETE  "$1" | grep -q "200 OK"; then curl -s -L --get "$1"; fi
