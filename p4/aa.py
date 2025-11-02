from c1 import *
def init_character(name="００００", exp=0):
    return {
        "name": name,
        "exp": exp,
        "items": ["なし"] * 8,
        "equips": [False] * 8
    }
def encode_items(items, equips):
    item_indices = [item_list.index(i) for i in items]
    equip_flags = [1 if e else 0 for e in equips]
    item_indices, equip_flags = remove_elements(item_indices, equip_flags)
    encoded = [f"{e:01b}{i:06b}" for i, e in zip(item_indices, equip_flags)]
    return encoded, f"{len(item_indices):04b}"
def remove_elements(items, equips):
    if 0 not in items: return items, equips
    index = items.index(0)
    return items[:index], equips[:index]
def split_string(string):
    chunks = [string[i:i+8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8: chunks[-1] = chunks[-1].ljust(8, '0')
    return chunks
ro = init_character()
sa = init_character()
mu = init_character()
flags = {
    "saFlag": False,
    "muFlag": False,
    "gold": 0,
    "town": town_list.index("ローレシア"),
    "flagMoon": moon_list.index("使っていない"),
    "flagGate": gate_list.index("開けていない"),
    "flagPlumage": plumage_list.index("織ってもらっていない"),
    "statShip": ship_list.index("何もしていない"),
    "statPrince": prince_list.index("見つけていない"),
    "crests": [False] * 5,
    "pattern": 0,
    "check": 0
}
BIroName = [nameToBinary(c) for c in ro["name"]]
BIroExp = f"{ro['exp']:020b}"
BIroItems, BIroItemsLen = encode_items(ro["items"], ro["equips"])
BIsaFlag = f"{int(flags['saFlag']):01b}"
BImuFlag = f"{int(flags['muFlag']):01b}"
BIsaExp = f"{sa['exp']:020b}"
BIsaItems, BIsaItemsLen = encode_items(sa["items"], sa["equips"])
BImuExp = f"{mu['exp']:020b}"
BImuItems, BImuItemsLen = encode_items(mu["items"], mu["equips"])
BIgold = f"{flags['gold']:016b}"
BItown = f"{flags['town']:03b}"
BIflagMoon = f"{flags['flagMoon']:01b}"
BIflagGate = f"{flags['flagGate']:01b}"
BIflagPlumage = f"{flags['flagPlumage']:01b}"
BIstatShip = f"{flags['statShip']:02b}"
BIstatPrince = f"{flags['statPrince']:02b}"
BIcrests = ''.join([f"{int(c):01b}" for c in flags["crests"]])
BIpattern = f"{flags['pattern']:04b}"
BIcheck = f"{flags['check']:08b}"
def build_bytes_str():
    base = (
        "00000" + BItown +
        BIroName[2] + BIroName[1][:2] +
        BIgold[:8] +
        BIroName[1][3:5] + BIroName[0] +
        BIgold[8:] +
        BIroName[1][5] + BIroName[3] + BIroName[1][2] +
        BIpattern[3] + BIflagMoon + BIflagGate + BIflagPlumage + BIstatShip + BIstatPrince +
        BIpattern[:3] + BIcrests +
        "00000000" +
        BIroExp[4:] + BIroExp[:4] + BIroItemsLen + ''.join(BIroItems) +
        BIsaFlag
    )
    if flags["saFlag"]:
        base += BIsaExp[4:] + BIsaExp[:4] + BIsaItemsLen + ''.join(BIsaItems) + BImuFlag
        if flags["muFlag"]: base += BImuExp[4:] + BImuExp[:4] + BImuItemsLen + ''.join(BImuItems)
    return base
def aa(pa):
  global BIpattern
  BIpattern=f"{pa:04b}"
  bytes_str = build_bytes_str()
  bytes = split_string(bytes_str)
  if len(bytes) == 40: bytes[8] = bytes[39]
  crc = calculate_crc(bytes)
  bytes[0] = crc[6:] + bytes[0][5:]
  bytes[8] = bytes[8][:2] + crc[:6]
  combined_str = ''.join(bytes)
  remainder = len(combined_str) % 6
  if remainder > 0: combined_str += '0' * (6 - remainder)
  password = [combined_str[i:i+6] for i in range(0, len(combined_str), 6)]
  nShift = int(password[0][3:5], 2) + 1
  print(' '.join(password))
  for i in range(1, len(password)): password[i] = f"{((int(password[i], 2) + int(password[i - 1], 2) + nShift) & 0x3f):06b}"
  jumon = ''.join([passDict[int(p, 2)] for p in password]) + '\n'
  print(' '.join(password))
  print(jumon, end="")
for i in range(1):aa(i)
