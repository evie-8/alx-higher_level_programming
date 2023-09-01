#!/usr/bin/python3
"""interview questions for holberton"""


if __name__ == "__main__":
    from sys import argv
    import requests

    try:
        url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
        data = requests.get(url)
        commits = data.json()

        for commit in commits[:10]:
            print(commit.get('sha'), end=": ")
            print(commit.get('commit').get('author').get('name'))
    except ValueError as e:
        pass
