
import json

# case1.json読み込み
with open("case1.json", "r", encoding="utf-8") as f:
    data = json.load(f)

numbers = data["numbers"]

# 差分計算
diff_list = []
prev = 0
for i, num in enumerate(numbers):
    diff_list.append({
        "index_from": i,
        "dec_from": num,
        "diff": num - prev
    })
    prev = num

# JSON保存
with open("case2.json", "w", encoding="utf-8") as f:
    json.dump({"diff": diff_list}, f, ensure_ascii=False, indent=2)
