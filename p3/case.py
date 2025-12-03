
import json

# a1.txtから呪文を読み込む
with open("a1.txt", "r", encoding="utf-8") as f:
    spell_text = f.read().strip()  # 改行や空白を除去
    spell = list(spell_text)       # 1文字ずつリスト化

# 対応表
passDict = {
    0:"あ", 1:"い", 2:"う", 3:"え", 4:"お", 5:"か", 6:"き", 7:"く", 8:"け", 9:"こ",
    10:"さ", 11:"し", 12:"す", 13:"せ", 14:"そ", 15:"た", 16:"ち", 17:"つ", 18:"て", 19:"と",
    20:"な", 21:"に", 22:"ぬ", 23:"ね", 24:"の", 25:"は", 26:"ひ", 27:"ふ", 28:"へ", 29:"ほ",
    30:"ま", 31:"み", 32:"む", 33:"め", 34:"も", 35:"や", 36:"ゆ", 37:"よ", 38:"ら", 39:"り",
    40:"る", 41:"れ", 42:"ろ", 43:"わ", 44:"が", 45:"ぎ", 46:"ぐ", 47:"げ", 48:"ご", 49:"ざ",
    50:"じ", 51:"ず", 52:"ぜ", 53:"ぞ", 54:"ば", 55:"び", 56:"ぶ", 57:"べ", 58:"ぼ", 59:"ぱ",
    60:"ぴ", 61:"ぷ", 62:"ぺ", 63:"ぽ"
}

# 逆引き辞書
reverseDict = {v: k for k, v in passDict.items()}

# 数値変換
numbers = [reverseDict[ch] for ch in spell]

# JSON保存
with open("case1.json", "w", encoding="utf-8") as f:
    json.dump({"numbers": numbers}, f, ensure_ascii=False, indent=2)


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


import json

# case2.json読み込み
with open("case2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

filtered = [item for item in data["diff"] if item["diff"] != 2]

# JSON保存
with open("case3.json", "w", encoding="utf-8") as f:
    json.dump({"diff": filtered}, f, ensure_ascii=False, indent=2)
