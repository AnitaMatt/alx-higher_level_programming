#!/bin/bash
#sets header variable and displays body response
curl -s "$1" -X GET  -H  "X-School-User-Id:98"
