#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url)

    datas = data.text
    print("Body response:")
    print(f"\t- type: {type(datas)}")
    print(f"\t- content: {datas}")
