key_map = {
    "index_from": "インデックス",
    "dec_from": "値",
    "diff": "差分"
}
data = {
    "diff": [
        {"index_from": 0, "dec_from": 58, "diff": 58},
        {"index_from": 3, "dec_from": 0, "diff": -62},
        {"index_from": 11, "dec_from": 4, "diff": -10}
    ]
}
converted = []
for item in data["diff"]:
    converted.append({key_map.get(k, k): v for k, v in item.items()})
for row in converted:
    print(row)
