#!/usr/bin/python3
"""sends a request and didplays the body"""

import sys
import urllib.request
import urllib.error

if __name__ == '__main':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
