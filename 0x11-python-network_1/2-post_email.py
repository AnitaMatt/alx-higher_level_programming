#!/usr/bin/python3
<<<<<<< HEAD

""" post an email"""
=======
"""make a post request """
>>>>>>> 82ebe6649c3f3440a2d83fc2ea646aebd23a7b19

import urllib.request
import urllib.parse
import sys

value = {'email':  sys.argv[2]}

data = urllib.parse.urlencode(value)

data = data.encode('ascii')

req = urllib.request.Request(sys.argv[1], data)

with urllib.request.urlopen(req) as res:
    print(res.read().decode('utf-8'))
