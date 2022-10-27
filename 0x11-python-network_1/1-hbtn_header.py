#!/usr/bin/python3
"""displays the value of the X-Request-Id variable in the header"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    print(dict(res.headers).get("X-Request-Id"))
