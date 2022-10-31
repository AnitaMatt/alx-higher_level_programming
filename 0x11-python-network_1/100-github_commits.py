#!/usr/bin/python3
"""Request commits via GitHub API
"""

import requests
from sys import argv

if __name__ == '__main__':

    repo = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/\
commits'.format(owner, repo)

    r = requests.get(url)

    r = r.json()
    

    try:
        for i in range(10):
            print('{}: {}'.format(r[i].get('sha'),
                              r[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
