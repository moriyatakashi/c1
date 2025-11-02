from a import*

_roItems = [roItem1, roItem2, roItem3, roItem4, roItem5, roItem6, roItem7, roItem8]
_roEquip = [roItem1Equip, roItem2Equip, roItem3Equip, roItem4Equip, roItem5Equip, roItem6Equip, roItem7Equip, roItem8Equip]

_saItems = [saItem1, saItem2, saItem3, saItem4, saItem5, saItem6, saItem7, saItem8]
_saEquip = [saItem1Equip, saItem2Equip, saItem3Equip, saItem4Equip, saItem5Equip, saItem6Equip, saItem7Equip, saItem8Equip]

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
             \
             BIroName[1][3:5]+ BIroName[0]+ \
             BIgold[8:]+ \
             BIroName[1][5]    + BIroName[3]       + BIroName[1][2]+ \
             \
             BIpattern[3] + BIflagMoon + BIflagGate + BIflagPlumage + BIstatShip + BIstatPrince+ \
             BIpattern[0:3]   + BIcrestLife      + BIcrestWater + BIcrestMoon + BIcrestStar + BIcrestSun+ \
             "00000000"+ \
             \
             BIroExp[4:]+ \
             BIroExp[0:4]      + BIroItemsLen+ \
             "".join(BIroItems)+ \
             \
             BIsaFlag
if saFlag:
  bytes_str += BIsaExp[4:]+ \
             BIsaExp[0:4] + BIsaItemsLen + \
             "".join(BIsaItems)+ \
             \
             BImuFlag
  if muFlag:
    bytes_str += BImuExp[4:]+ \
             BImuExp[0:4] + BImuItemsLen + \
             "".join(BImuItems)
bytes = split_string(bytes_str)
if(len(bytes) == 40):
  bytes[8] = bytes[39]
  del bytes[39]
bytes_str =     "00000"        + BItown + \
             BIroName[2]    + BIroName[1][:2]+ \
             BIgold[:8]+ \
             \
             BIroName[1][3:5]+ BIroName[0]+ \
             BIgold[8:]+ \
             BIroName[1][5]    + BIroName[3]       + BIroName[1][2]+ \
             \
             BIpattern[3] + BIflagMoon + BIflagGate + BIflagPlumage + BIstatShip + BIstatPrince+ \
             BIpattern[0:3]   + BIcrestLife      + BIcrestWater + BIcrestMoon + BIcrestStar + BIcrestSun+ \
             "00000000"+ \
             \
             BIroExp[4:]+ \
             BIroExp[0:4]      + BIroItemsLen+ \
             "".join(BIroItems)+ \
             \
             BIsaFlag
if saFlag:
  bytes_str += BIsaExp[4:]+ \
             BIsaExp[0:4] + BIsaItemsLen + \
             "".join(BIsaItems)+ \
             \
             BImuFlag
  if muFlag:
    bytes_str += BImuExp[4:]+ \
             BImuExp[0:4] + BImuItemsLen + \
             "".join(BImuItems)
bytes = split_string(bytes_str)
if(len(bytes) == 40):
  bytes[8] = bytes[39]
  del bytes[39]
bytes_str =     "00000"        + BItown + \
             BIroName[2]    + BIroName[1][:2]+ \
             BIgold[:8]+ \
             \
             BIroName[1][3:5]+ BIroName[0]+ \
             BIgold[8:]+ \
             BIroName[1][5]    + BIroName[3]       + BIroName[1][2]+ \
             \
             BIpattern[3] + BIflagMoon + BIflagGate + BIflagPlumage + BIstatShip + BIstatPrince+ \
             BIpattern[0:3]   + BIcrestLife      + BIcrestWater + BIcrestMoon + BIcrestStar + BIcrestSun+ \
             "00000000"+ \
             \
             BIroExp[4:]+ \
             BIroExp[0:4]      + BIroItemsLen+ \
             "".join(BIroItems)+ \
             \
             BIsaFlag
if saFlag:
  bytes_str += BIsaExp[4:]+ \
             BIsaExp[0:4] + BIsaItemsLen + \
             "".join(BIsaItems)+ \
             \
             BImuFlag
  if muFlag:
    bytes_str += BImuExp[4:]+ \
             BImuExp[0:4] + BImuItemsLen + \
             "".join(BImuItems)
bytes = split_string(bytes_str)
if(len(bytes) == 40):
  bytes[8] = bytes[39]
  del bytes[39]
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
jumon = shape_jumon(jumon)
print(jumon)
