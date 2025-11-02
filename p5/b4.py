pass_list = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞばびぶべぼぱぴぷぺぽ")
name_list = list("０１２３４５６７８９あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんっゃゅょ゛゜　")
def to_bin(char, table): return format(table.index(char), "06b")
def shape_jumon(s): return '\n'.join(['  '.join([s[i:i+3], s[i+3:i+6], s[i+6:i+9]]) for i in range(0, len(s), 10)])
def split8(s): return [s[i:i+8].ljust(8, '0') for i in range(0, len(s), 8)]
def crc_calc(code):
    crc = len(code) * 0x0101
    for i in reversed(range(len(code))):
        octet = int(code[i], 2)
        for _ in range(8):
            carry = ((crc >> 8) ^ octet) & 0x80
            crc = (crc << 1) & 0xffff
            octet = (octet << 1) & 0xff
            if carry: crc ^= 0x1021
    return format(crc & 0x07ff, "011b")
def init_char(exp, items, equips):
    ids = [item_list.index(i) for i in items if i]
    flags = [1 if equips[i] else 0 for i in range(len(ids))]
    bin_items = [f"{e}{i:06b}" for i, e in zip(ids, flags)]
    return {"exp": format(exp, "020b"), "items": bin_items, "items_len": format(len(bin_items), "04b")}
def flags_bin(data):
    return {
        "town": format(town_list.index(data["_town"]), "03b"),
        "moon": format(moon_list.index(data["_flagMoon"]), "01b"),
        "gate": format(gate_list.index(data["_flagGate"]), "01b"),
        "plumage": format(plumage_list.index(data["_flagPlumage"]), "01b"),
        "ship": format(ship_list.index(data["_statShip"]), "02b"),
        "prince": format(prince_list.index(data["_statPrince"]), "02b"),
        "crests": ''.join(['1' if data[f"_crest{c}"] else '0' for c in ["Life", "Water", "Moon", "Star", "Sun"]]),
        "pattern": format(data["pattern"], "04b"),
        "check": format(data["check"], "08b"),
        "gold": format(data["gold"], "016b")
    }
roName = "００００"
roExp = saExp = muExp = 0
saFlag = muFlag = False
gold = pattern = check = 0
_town = _flagMoon = _flagGate = _flagPlumage = _statShip = _statPrince = ""
_crestLife = _crestWater = _crestMoon = _crestStar = _crestSun = False
item_list = town_list = moon_list = gate_list = plumage_list = ship_list = prince_list = [""]
empty_items = [""] * 8
empty_equips = [False] * 8
BIroName = [to_bin(c, name_list) for c in roName]
ro = init_char(roExp, empty_items, empty_equips)
sa = init_char(saExp, empty_items, empty_equips)
mu = init_char(muExp, empty_items, empty_equips)
flags = flags_bin({
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
bytes = split8(bytes_str)
if len(bytes) == 40:
    bytes[8] = bytes[39]
    del bytes[39]
crc = crc_calc(bytes)
bytes[0] = crc[6:] + bytes[0][5:]
bytes[8] = bytes[8][:2] + crc[:6]
combined = ''.join(bytes)
combined += '0' * ((6 - len(combined) % 6) % 6)
password = [combined[i:i+6] for i in range(0, len(combined), 6)]
nShift = int(password[0][3:5], 2) + 1
for i in range(1, len(password)):
    password[i] = format((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3f, "06b")
jumon = ''.join([pass_list[int(p, 2)] for p in password])
print(shape_jumon(jumon))
