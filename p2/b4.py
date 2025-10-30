import sys
import json
pa=open(sys.argv[1]).read()
pb=json.loads(pa)
print(pb)