from a2 import *
roName = "００００"
roExp = saExp = muExp = 0
saFlag = muFlag = False
gold = pattern = check = 0
_town = "ローレシア"
_flagMoon = "使っていない"
_flagGate = "開けていない"
_flagPlumage = "織ってもらっていない"
_statShip = "何もしていない"
_statPrince = "見つけていない"
_crestLife = _crestWater = _crestMoon = _crestStar = _crestSun = False
empty_items = ["なし"] * 8
empty_equips = [False] * 8
BIroName = [nameToBinary(c) for c in roName]
ro = init_character(roName, roExp, empty_items, empty_equips)
sa = init_character("サマルトリア", saExp, empty_items, empty_equips)
mu = init_character("ムーンブルク", muExp, empty_items, empty_equips)
flags = convert_flags({
    "_town": _town, "_flagMoon": _flagMoon, "_flagGate": _flagGate, "_flagPlumage": _flagPlumage,
    "_statShip": _statShip, "_statPrince": _statPrince,
    "_crestLife": _crestLife, "_crestWater": _crestWater, "_crestMoon": _crestMoon,
    "_crestStar": _crestStar, "_crestSun": _crestSun,
    "pattern": pattern, "check": check, "gold": gold
})
bytes_str = (
    "00000" + flags["town"] + BIroName[2] + BIroName[1][:2] + flags["gold"][:8] +
    BIroName[1][3:5] + BIroName[0] + flags["gold"][8:] + BIroName[1][5] + BIroName[3] + BIroName[1][2] +
    flags["pattern"][3] + flags["moon"] + flags["gate"] + flags["plumage"] + flags["ship"] + flags["prince"] + flags["pattern"][:3] +
    flags["crests"] + "00000000" + ro["exp"][4:] + ro["exp"][:4] + ro["items_len"] + ''.join(ro["items"]) + format(saFlag, "01b")
)
if saFlag:
    bytes_str += sa["exp"][4:] + sa["exp"][:4] + sa["items_len"] + ''.join(sa["items"]) + format(muFlag, "01b")
    if muFlag:
        bytes_str += mu["exp"][4:] + mu["exp"][:4] + mu["items_len"] + ''.join(mu["items"])
bytes = split_string(bytes_str)
if len(bytes) == 40:
    bytes[8] = bytes[39]
    del bytes[39]
crc = calculate_crc(bytes)
bytes[0] = crc[6:] + bytes[0][5:]
bytes[8] = bytes[8][:2] + crc[:6]
combined_str = ''.join(bytes)
remainder = len(combined_str) % 6
if remainder > 0:
    combined_str += '0' * (6 - remainder)
password = [combined_str[i:i+6] for i in range(0, len(combined_str), 6)]
nShift = int(password[0][3:5], 2) + 1
for i in range(1, len(password)):
    password[i] = format((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3f, "06b")
jumon = ''.join([passDict[int(p, 2)] for p in password])
jumon = shape_jumon(jumon)
print(crc)
print(jumon)