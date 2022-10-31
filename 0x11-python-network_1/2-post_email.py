#!/usr/bin/python3

"""Make a POST request
"""

import urllib.request
import urllib.parse
import sys

value = {'email':  sys.argv[2]}

data = urllib.parse.urlencode(value)

data = data.encode('ascii')

req = urllib.request.Request(sys.argv[1], data)

with urllib.request.urlopen(req) as res:
    print(res.read().decode('utf-8'))
