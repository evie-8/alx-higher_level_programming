#!/usr/bin/python3
"""a Python script that
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import sys
    import requests
    import requests.auth

    url = f'https://api.github.com/users/{sys.argv[1]}'
    data = requests.get(url,
                        auth=requests.auth.HTTPBasicAuth(
                            sys.argv[1], sys.argv[2]))
    print(data.json().get('id'))
