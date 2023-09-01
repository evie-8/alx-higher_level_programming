#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
 curl -s -I "$1" | sed -n '/Content-Length/p' | cut -d ':' -f 2 
