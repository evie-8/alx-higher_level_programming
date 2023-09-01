#!/usr/bin/python3
"""a Python script
that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    data = requests.post(url, data={'q': q})

    try:
        dicts = data.json()
        id, name = dicts.get('id'), dicts.get('name')

        if len(dicts) == 0 or not name or not id:
            print("No result")
        else:
            print(f"[{id}] {name}")
    except Exception:
        print("Not a valid JSON")
