roName = "００００" 
assert len(roName) == 4, print("エラー：なまえは全角空白を含め4文字で入力してください。")
roExp = 0 
roItem1 = "なし" 
roItem1Equip = False 
roItem2 = "なし" 
roItem2Equip = False 
roItem3 = "なし" 
roItem3Equip = False 
roItem4 = "なし" 
roItem4Equip = False 
roItem5 = "なし" 
roItem5Equip = False 
roItem6 = "なし" 
roItem6Equip = False 
roItem7 = "なし" 
roItem7Equip = False 
roItem8 = "なし" 
roItem8Equip = False 
_roItems = [roItem1, roItem2, roItem3, roItem4, roItem5, roItem6, roItem7, roItem8]
_roEquip = [roItem1Equip, roItem2Equip, roItem3Equip, roItem4Equip, roItem5Equip, roItem6Equip, roItem7Equip, roItem8Equip]
saFlag = False 
saExp = 0 
saItem1 = "なし" 
saItem1Equip = False 
saItem2 = "なし" 
saItem2Equip = False 
saItem3 = "なし" 
saItem3Equip = False 
saItem4 = "なし" 
saItem4Equip = False 
saItem5 = "なし" 
saItem5Equip = False 
saItem6 = "なし" 
saItem6Equip = False 
saItem7 = "なし" 
saItem7Equip = False 
saItem8 = "なし" 
saItem8Equip = False 
_saItems = [saItem1, saItem2, saItem3, saItem4, saItem5, saItem6, saItem7, saItem8]
_saEquip = [saItem1Equip, saItem2Equip, saItem3Equip, saItem4Equip, saItem5Equip, saItem6Equip, saItem7Equip, saItem8Equip]
muFlag = False 
muExp = 0 
muItem1 = "なし" 
muItem1Equip = False 
muItem2 = "なし" 
muItem2Equip = False 
muItem3 = "なし" 
muItem3Equip = False 
muItem4 = "なし" 
muItem4Equip = False 
muItem5 = "なし" 
muItem5Equip = False 
muItem6 = "なし" 
muItem6Equip = False 
muItem7 = "なし" 
muItem7Equip = False 
muItem8 = "なし" 
muItem8Equip = False 
_muItems = [muItem1, muItem2, muItem3, muItem4, muItem5, muItem6, muItem7, muItem8]
_muEquip = [muItem1Equip, muItem2Equip, muItem3Equip, muItem4Equip, muItem5Equip, muItem6Equip, muItem7Equip, muItem8Equip]
gold = 0 
_town = "ローレシア" 
_flagMoon = "使っていない" 
_flagGate = "開けていない" 
_flagPlumage = "織ってもらっていない" 
_statShip = "何もしていない" 
_statPrince = "見つけていない" 
_crestLife = False 
_crestWater = False 
_crestMoon = False 
_crestStar = False 
_crestSun = False 
pattern = 0 
check = 0
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
item_list = ["なし", "ひのきのぼう", "せいなるナイフ", "まどうしのつえ", "いかずちのつえ", "こんぼう", "どうのつるぎ", "くさりがま","てつのやり", "はやぶさのけん", "はがねのつるぎ", "おおかなずち", "はかいのつるぎ", "ドラゴンキラー", "ひかりのつるぎ","ロトのつるぎ", "いなずまのけん", "ぬののふく", "みかわしのふく", "みずのはごろも", "ミンクのコート", "かわのよろい","くさりかたびら", "あくまのよろい", "まほうのよろい", "はがねのよろい", "ガイアのよろい", "ロトのよろい", "かわのたて", "ちからのたて", "はがねのたて", "しにがみのたて", "ロトのたて", "ふしぎなかぶと", "てつかぶと", "ロトのかぶと", "ロトのしるし", "ふねのざいほう", "つきのかけら", "ルビスのまもり", "じゃしんのぞう", "せかいじゅのは", "やまびこのふえ", "ラーのかがみ","あまつゆのいと", "せいなるおりき", "かぜのマント", "あくまのしっぽ", "まよけのすず", "ふっかつのたま", "ゴールドカード", "ふくびきけん", "せいすい", "キメラのつばさ", "みみせん（使用不可）", "きんのかぎ","ぎんのかぎ", "ろうやのかぎ", "すいもんのかぎ", "どくけしそう", "やくそう", "いのりのゆびわ", "しのオルゴール（使用不可）","あぶないみずぎ（MSX専用）"]
town_list = ["ローレシア", "サマルトリア", "ラダトーム", "デルコンダル","ベラヌール", "ロンダルキア", "ムーンペタ", "（不正）"]
moon_list = ["使っていない", "使った"]
gate_list = ["開けていない", "開けた"]
plumage_list = ["織ってもらっていない", "織ってもらった"]
ship_list = ["何もしていない", "女の子を助けた", "船をもらった（通常プレイではありえない）", "船をもらった"]
prince_list = ["見つけていない", "探して、王様に会った", "探して、勇者の泉に行った", "見つけた"]
roItems = [item_list.index(i) for i in _roItems]
roEquip = [1 if i else 0 for i in _roEquip]
saItems = [item_list.index(i) for i in _saItems]
saEquip = [1 if i else 0 for i in _saEquip]
muItems = [item_list.index(i) for i in _muItems]
muEquip = [1 if i else 0 for i in _muEquip]
town = town_list.index(_town)
flagMoon = moon_list.index(_flagMoon)
flagGate = gate_list.index(_flagGate)
flagPlumage = plumage_list.index(_flagPlumage)
statShip = ship_list.index(_statShip)
statPrince = prince_list.index(_statPrince)
crestLife = 1 if _crestLife else 0
crestWater = 1 if _crestWater else 0
crestMoon = 1 if _crestMoon else 0
crestStar = 1 if _crestStar else 0
crestSun = 1 if _crestSun else 0
BIroName = [nameToBinary(char) for char in roName]
roItems, roEquip = remove_elements(roItems, roEquip)
BIroItems = [format(equip, "01b") + format(item, "06b") for item, equip in zip(roItems, roEquip)]
BIroItemsLen = format(len(roItems), "04b")
BIroExp = format(roExp, "020b")
BIsaFlag = format(saFlag, "01b")
saItems, saEquip = remove_elements(saItems, saEquip)
BIsaItems = [format(equip, "01b") + format(item, "06b") for item, equip in zip(saItems, saEquip)]
BIsaItemsLen = format(len(saItems), "04b")
BIsaExp = format(saExp, "020b")
BImuFlag = format(muFlag, "01b")
muItems, muEquip = remove_elements(muItems, muEquip)
BImuItems = [format(equip, "01b") + format(item, "06b") for item, equip in zip(muItems, muEquip)]
BImuItemsLen = format(len(muItems), "04b")
BImuExp = format(muExp, "020b")
BIgold = format(gold, "016b")
BItown = format(town, "03b")
BIflagMoon = format(flagMoon, "01b")
BIflagGate = format(flagGate, "01b")
BIflagPlumage = format(flagPlumage, "01b")
BIstatShip = format(statShip, "02b")
BIstatPrince = format(statPrince, "02b")
BIcrestLife = format(crestLife, "01b")
BIcrestWater = format(crestWater, "01b")
BIcrestMoon = format(crestMoon, "01b")
BIcrestStar = format(crestStar, "01b")
BIcrestSun = format(crestSun, "01b")
BIpattern = format(pattern, "04b")
BIcheck = format(check, "08b")
bytes_str =     "00000"        + BItown + \
             BIroName[2]    + BIroName[1][:2]+ \
             BIgold[:8]+ \
             BIroName[1][3:5]+ BIroName[0]+ \
             BIgold[8:]+ \
             BIroName[1][5]    + BIroName[3]       + BIroName[1][2]+ \
             BIpattern[3] + BIflagMoon + BIflagGate + BIflagPlumage + BIstatShip + BIstatPrince+ \
             BIpattern[0:3]   + BIcrestLife      + BIcrestWater + BIcrestMoon + BIcrestStar + BIcrestSun+ \
             "00000000"+ \
             BIroExp[4:]+ \
             BIroExp[0:4]      + BIroItemsLen+ \
             "".join(BIroItems)+ \
             BIsaFlag
bytes = split_string(bytes_str)
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
crc = calculate_crc(bytes)
bytes[0] = crc[6:] + bytes[0][5:]
bytes[8] = bytes[8][:2] + crc[:6]
print(crc)
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
print(jumon)
