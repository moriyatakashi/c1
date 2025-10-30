#!/bin/python3
import json
pa=json.loads(open("/home/a/a1/z1/a.json").read())
print("Content-Type: text/html\n\n"+str(pa))