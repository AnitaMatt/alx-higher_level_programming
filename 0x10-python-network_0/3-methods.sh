#!/bin/bash
# get all allow methods
curl -sI "$1"| grep "Allow" | cut -d ' ' -f1  --complement
