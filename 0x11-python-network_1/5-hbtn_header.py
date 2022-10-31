#!/usr/bin/python3
"""sends a post request eith request package"""

import requests
import sys

url = sys.argv[1]

res = requests.get(url)
r = res.headers
print(r.get('X-Request-Id'))
