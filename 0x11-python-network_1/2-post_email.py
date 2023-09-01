#!/usr/bin/python3
"""script that takes in a URL
sends a request to the URL and email"""

if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    dicts = {"email": email}
    data = urllib.parse.urlencode(dicts).encode('ascii')

    f = urllib.request.Request(url, data)
    with urllib.request.urlopen(f) as file:
        value = file.read().decode('utf-8')
    print(value)
