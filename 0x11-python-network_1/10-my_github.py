#!/usr/bin/python3
"""a Python script that
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    data = requests.get(url,
                        auth=HTTPBasicAuth(argv[1], argv[2]))
    print(data.json().get('id'))
