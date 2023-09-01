#!/usr/bin/python3
"""errors"""


if __name__ == "__main__":
    import sys
    from urllib import error, request

    try:
        url = sys.argv[1]
        with request.urlopen(url) as message:
            print(message.read().decode("utf-8"))
    except error.HTTPError as errors:
        print("Error code:", error.code)
