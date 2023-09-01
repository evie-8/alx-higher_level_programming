#!/usr/bin/python3
"""getting header element"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    data = requests.get(url)
    value = data.headers.get('X-Request-Id')
    print(value)
