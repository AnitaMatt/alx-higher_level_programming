#!/usr/bin/python3
"""getting header data"""

import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    print(dict(res.headers).get("X-Request-Id"))
