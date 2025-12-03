roName = "００００"
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
_roEquip = [
    roItem1Equip,
    roItem2Equip,
    roItem3Equip,
    roItem4Equip,
    roItem5Equip,
    roItem6Equip,
    roItem7Equip,
    roItem8Equip,
]
saFlag = False
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
nameDict = {
    0: "０",
    1: "１",
    2: "２",
    3: "３",
    4: "４",
    5: "５",
    6: "６",
    7: "７",
    8: "８",
    9: "９",
    10: "あ",
    11: "い",
    12: "う",
    13: "え",
    14: "お",
    15: "か",
    16: "き",
    17: "く",
    18: "け",
    19: "こ",
    20: "さ",
    21: "し",
    22: "す",
    23: "せ",
    24: "そ",
    25: "た",
    26: "ち",
    27: "つ",
    28: "て",
    29: "と",
    30: "な",
    31: "に",
    32: "ぬ",
    33: "ね",
    34: "の",
    35: "は",
    36: "ひ",
    37: "ふ",
    38: "へ",
    39: "ほ",
    40: "ま",
    41: "み",
    42: "む",
    43: "め",
    44: "も",
    45: "や",
    46: "ゆ",
    47: "よ",
    48: "ら",
    49: "り",
    50: "る",
    51: "れ",
    52: "ろ",
    53: "わ",
    54: "を",
    55: "ん",
    56: "っ",
    57: "ゃ",
    58: "ゅ",
    59: "ょ",
    60: "゛",
    61: "゜",
    62: "　",
}
def remove_elements(items, equip):
    if 0 not in items:
        return items, equip
    index = items.index(0)
    return items[:index], equip[:index]
def split_string(string):
    chunks = [string[i : i + 8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8:
        chunks[-1] = chunks[-1].ljust(8, "0")
    return chunks
item_list = [
    "なし",
    "ひのきのぼう",
    "せいなるナイフ",
    "まどうしのつえ",
    "いかずちのつえ",
    "こんぼう",
    "どうのつるぎ",
    "くさりがま",
    "てつのやり",
    "はやぶさのけん",
    "はがねのつるぎ",
    "おおかなずち",
    "はかいのつるぎ",
    "ドラゴンキラー",
    "ひかりのつるぎ",
    "ロトのつるぎ",
    "いなずまのけん",
    "ぬののふく",
    "みかわしのふく",
    "みずのはごろも",
    "ミンクのコート",
    "かわのよろい",
    "くさりかたびら",
    "あくまのよろい",
    "まほうのよろい",
    "はがねのよろい",
    "ガイアのよろい",
    "ロトのよろい",
    "かわのたて",
    "ちからのたて",
    "はがねのたて",
    "しにがみのたて",
    "ロトのたて",
    "ふしぎなかぶと",
    "てつかぶと",
    "ロトのかぶと",
    "ロトのしるし",
    "ふねのざいほう",
    "つきのかけら",
    "ルビスのまもり",
    "じゃしんのぞう",
    "せかいじゅのは",
    "やまびこのふえ",
    "ラーのかがみ",
    "あまつゆのいと",
    "せいなるおりき",
    "かぜのマント",
    "あくまのしっぽ",
    "まよけのすず",
    "ふっかつのたま",
    "ゴールドカード",
    "ふくびきけん",
    "せいすい",
    "キメラのつばさ",
    "みみせん（使用不可）",
    "きんのかぎ",
    "ぎんのかぎ",
    "ろうやのかぎ",
    "すいもんのかぎ",
    "どくけしそう",
    "やくそう",
    "いのりのゆびわ",
    "しのオルゴール（使用不可）",
    "あぶないみずぎ（MSX専用）",
]
town_list = [
    "ローレシア",
    "サマルトリア",
    "ラダトーム",
    "デルコンダル",
    "ベラヌール",
    "ロンダルキア",
    "ムーンペタ",
    "（不正）",
]
moon_list = ["使っていない", "使った"]
gate_list = ["開けていない", "開けた"]
plumage_list = ["織ってもらっていない", "織ってもらった"]
ship_list = [
    "何もしていない",
    "女の子を助けた",
    "船をもらった（通常プレイではありえない）",
    "船をもらった",
]
prince_list = [
    "見つけていない",
    "探して、王様に会った",
    "探して、勇者の泉に行った",
    "見つけた",
]
roItems = [item_list.index(i) for i in _roItems]
roEquip = [1 if i else 0 for i in _roEquip]
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
BIroItems = [
    format(equip, "01b") + format(item, "06b") for item, equip in zip(roItems, roEquip)
]
BIroItemsLen = format(len(roItems), "04b")
BIroExp = format(roExp, "020b")
BIsaFlag = format(saFlag, "01b")
BIgold = format(gold, "016b")
# BItown = format(town, "03b")
BItown = "110"
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
bytes_str = (
    "00000"
    + BItown
    + BIroName[2]
    + BIroName[1][:2]
    + BIgold[:8]
    + BIroName[1][3:5]
    + BIroName[0]
    + BIgold[8:]
    + BIroName[1][5]
    + BIroName[3]
    + BIroName[1][2]
    + BIpattern[3]
    + BIflagMoon
    + BIflagGate
    + BIflagPlumage
    + BIstatShip
    + BIstatPrince
    + BIpattern[0:3]
    + BIcrestLife
    + BIcrestWater
    + BIcrestMoon
    + BIcrestStar
    + BIcrestSun
    + "00000000"
    + BIroExp[4:]
    + BIroExp[0:4]
    + BIroItemsLen
    + "".join(BIroItems)
    + BIsaFlag
)
bytes = split_string(bytes_str)
