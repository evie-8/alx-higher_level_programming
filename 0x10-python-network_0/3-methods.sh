#!/bin/bash
#  a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I -L -X OPTIONS "$1" | sed -n '/Allow:/ p' | cut -d ":" -f 2 | sed 's/^[[:space:]]*//'
