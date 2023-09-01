#!/usr/bin/python3
"""script to  get error code"""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    data = requests.get(url)
    statusCode = data.status_code

    if statusCode < 400:
        print(data.text)
    else:
        print(f"Error code: {statusCode}")
