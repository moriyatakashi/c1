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
_crestLife = False  
_crestWater = False  
_crestMoon = False  
_crestStar = False  
_crestSun = False  
pattern = 0  
check = 0
passDict = {
    0: "あ",
    1: "い",
    2: "う",
    3: "え",
    4: "お",
    5: "か",
    6: "き",
    7: "く",
    8: "け",
    9: "こ",
    10: "さ",
    11: "し",
    12: "す",
    13: "せ",
    14: "そ",
    15: "た",
    16: "ち",
    17: "つ",
    18: "て",
    19: "と",
    20: "な",
    21: "に",
    22: "ぬ",
    23: "ね",
    24: "の",
    25: "は",
    26: "ひ",
    27: "ふ",
    28: "へ",
    29: "ほ",
    30: "ま",
    31: "み",
    32: "む",
    33: "め",
    34: "も",
    35: "や",
    36: "ゆ",
    37: "よ",
    38: "ら",
    39: "り",
    40: "る",
    41: "れ",
    42: "ろ",
    43: "わ",
    44: "が",
    45: "ぎ",
    46: "ぐ",
    47: "げ",
    48: "ご",
    49: "ざ",
    50: "じ",
    51: "ず",
    52: "ぜ",
    53: "ぞ",
    54: "ば",
    55: "び",
    56: "ぶ",
    57: "べ",
    58: "ぼ",
    59: "ぱ",
    60: "ぴ",
    61: "ぷ",
    62: "ぺ",
    63: "ぽ",
}

from aab import *
roItems = [0 for i in _roItems]
roEquip = [1 if i else 0 for i in _roEquip]
town = 0
flagMoon = 0
flagGate = 0
flagPlumage = 0
statShip = 0
statPrince = 0
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
aaa(bytes_str, "b9.json")
aaa(bytes, "b8.json")
if len(bytes) == 40:
    print("pass1")
    bytes[8] = bytes[39]
    del bytes[39]
crc = calculate_crc(bytes)
aaa(crc, "b7.json")
bytes[0] = crc[6:] + bytes[0][5:]
bytes[8] = bytes[8][:2] + crc[:6]
aaa(bytes, "b6.json")
password = []
combined_str = "".join(bytes)
remainder = len(combined_str) % 6
if remainder > 0:
    combined_str += "0" * (6 - remainder)
aaa(combined_str, "b5.json")
password = [combined_str[i : i + 6] for i in range(0, len(combined_str), 6)]
nShift = int(password[0][3:5], 2) + 1
aaa(nShift, "b4.json")
aaa(password, "b3.json")
for i in range(1, len(password)):
    password[i] = format(
        ((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3F), "06b"
    )
aaa(password, "b2.json")
jumon = ""
passTemp = password.copy()
for i in range(len(password)):
    char = passTemp.pop(0)
    jumon += passDict[int(char, 2)]
aaa(jumon, "b1.json")
