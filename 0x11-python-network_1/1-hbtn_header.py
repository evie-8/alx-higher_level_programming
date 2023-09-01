#!/usr/bin/python3
"""script that takes in a URL
sends a request to the URL
displays value of X-Request-Id variable found in header of response."""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    f = urllib.request.Request(url)
    with urllib.request.urlopen(f) as file:
        value = dict(file.headers).get('X-Request-Id')
    print(value)
