#!/bin/bash
# Getting the size of the body response
curl -sI "$1" | grep "Content-Length" | cut -d  ' '  -f2
