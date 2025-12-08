from datetime import datetime
def aaa(text, filepath):
    print(text)
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text
    }
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
def aab(filepath):
    data = {
        "BItown": "000"
    }
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
def calculate_crc(code):
    crc = len(code) * 0x0101
    for i in range(len(code) - 1, -1, -1):
        octed = code[i]
        octed = int(octed, 2)  
        for j in range(8):
            carry_bit = ((crc >> 8) ^ octed) & 0x80 != 0
            crc = (crc << 1) & 0xffff
            octed = (octed << 1) & 0xff
            if carry_bit:
                crc ^= 0x1021
    return format(crc & 0x07ff, "011b")
def nameToBinary(char):
  key = [k for k, v in nameDict.items() if v == char][0]
  return format(key, "06b")
nameDict = {0:"０", 1:"１", 2:"２", 3:"３", 4:"４", 5:"５", 6:"６", 7:"７", 8:"８", 9:"９",
            10:"あ", 11:"い", 12:"う", 13:"え", 14:"お", 15:"か", 16:"き", 17:"く", 18:"け", 19:"こ",
            20:"さ", 21:"し", 22:"す", 23:"せ", 24:"そ", 25:"た", 26:"ち", 27:"つ", 28:"て", 29:"と",
            30:"な", 31:"に", 32:"ぬ", 33:"ね", 34:"の", 35:"は", 36:"ひ", 37:"ふ", 38:"へ", 39:"ほ",
            40:"ま", 41:"み", 42:"む", 43:"め", 44:"も", 45:"や", 46:"ゆ", 47:"よ", 48:"ら", 49:"り",
            50:"る", 51:"れ", 52:"ろ", 53:"わ", 54:"を", 55:"ん", 56:"っ", 57:"ゃ", 58:"ゅ", 59:"ょ",
            60:"゛", 61:"゜", 62:"　"}
passDict = {0:"あ", 1:"い", 2:"う", 3:"え", 4:"お", 5:"か", 6:"き", 7:"く", 8:"け", 9:"こ",
            10:"さ", 11:"し", 12:"す", 13:"せ", 14:"そ", 15:"た", 16:"ち", 17:"つ", 18:"て", 19:"と",
            20:"な", 21:"に", 22:"ぬ", 23:"ね", 24:"の", 25:"は", 26:"ひ", 27:"ふ", 28:"へ", 29:"ほ",
            30:"ま", 31:"み", 32:"む", 33:"め", 34:"も", 35:"や", 36:"ゆ", 37:"よ", 38:"ら", 39:"り",
            40:"る", 41:"れ", 42:"ろ", 43:"わ", 44:"が", 45:"ぎ", 46:"ぐ", 47:"げ", 48:"ご", 49:"ざ",
            50:"じ", 51:"ず", 52:"ぜ", 53:"ぞ", 54:"ば", 55:"び", 56:"ぶ", 57:"べ", 58:"ぼ", 59:"ぱ",
            60:"ぴ", 61:"ぷ", 62:"ぺ", 63:"ぽ"}
def remove_elements(items, equip):
    if 0 not in items:
        return items, equip
    index = items.index(0)
    return items[:index], equip[:index]
def split_string(string):
    chunks = [string[i:i+8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8:
        chunks[-1] = chunks[-1].ljust(8, '0')
    return chunks
def aa1(bytes_str):
  bytes = split_string(bytes_str)
  crc = calculate_crc(bytes)
  bytes[0] = crc[6:] + bytes[0][5:]
  bytes[8] = bytes[8][:2] + crc[:6]
  password = []
  combined_str = ''.join(bytes)
  remainder = len(combined_str) % 6
  if remainder > 0:
    combined_str += '0' * (6 - remainder)
  password = [combined_str[i:i+6] for i in range(0, len(combined_str), 6)]
  nShift = int(password[0][3:5], 2) + 1
  for i in range(1, len(password)):
    password[i] = format(((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3f), "06b")
  jumon = ""
  passTemp = password.copy()
  for i in range(len(password)):
    char = passTemp.pop(0) 
    jumon += passDict[int(char, 2)]
  return jumon
def ba1():
    with open("b1.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["BItown"]
def ba2(pa,pb):
    return pa+pb[len(pa)-1:]