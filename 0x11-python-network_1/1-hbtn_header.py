#!/usr/bin/python3
"""Request and parse header
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as res:
        print(dict(res.headers).get('X-Request-Id'))
