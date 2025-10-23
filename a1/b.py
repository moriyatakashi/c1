def b1():
    import json
    for pa in json.loads(open("a.json").read()):print(pa["c"])
