#!/usr/bin/python3
"""request headers"""

import requests
import sys

if __name__ = '__main__':
    url = sys.argv[1]

    res = requests.get(url)
    r = res.headers
    print(r.get('X-Request-Id'))
