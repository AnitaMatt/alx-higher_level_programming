#!/usr/bin/python3
"""Make a POST request
"""

import sys
import requests

url = sys.argv[1]
value = {'email': sys.argv[2]}

req = requests.post(url, data=value)
print(req.text)
