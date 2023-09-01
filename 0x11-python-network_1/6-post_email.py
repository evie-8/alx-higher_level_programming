#!/usr/bin/python3
"""passing a variable"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    dicts = {"email": email}
    data = requests.post(url, data=dicts)
    print(data.text)
