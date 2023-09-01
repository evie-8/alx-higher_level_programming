#!/bin/bash
# a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
 if curl -s -I -L "$1" | grep -q "200 OK"; then curl -s -L --get "$1"; fi
