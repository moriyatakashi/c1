
import json

# case2.json読み込み
with open("case2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

filtered = [item for item in data["diff"] if item["diff"] != 2]

# JSON保存
with open("case3.json", "w", encoding="utf-8") as f:
    json.dump({"diff": filtered}, f, ensure_ascii=False, indent=2)
