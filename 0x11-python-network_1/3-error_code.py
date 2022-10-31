#!/usr/bin/python3
"""sends a request and didplays the body"""

import sys
import urllib.request
import urllib.error

url = sys.argv[1]

req = urllib.request.Request(url)

try:
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
