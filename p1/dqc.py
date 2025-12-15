if 1:
  roName = "００００" 
  roExp = 0 
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
  def split_string(string):
    chunks = [string[i:i+8] for i in range(0, len(string), 8)]
    if len(chunks[-1]) < 8:
        chunks[-1] = chunks[-1].ljust(8, '0')
    return chunks
  town_list = ["ローレシア", "サマルトリア", "ラダトーム", "デルコンダル","ベラヌール", "ロンダルキア", "ムーンペタ", "（不正）"]
  moon_list = ["使っていない", "使った"]
  gate_list = ["開けていない", "開けた"]
  plumage_list = ["織ってもらっていない", "織ってもらった"]
  ship_list = ["何もしていない", "女の子を助けた", "船をもらった（通常プレイではありえない）", "船をもらった"]
  prince_list = ["見つけていない", "探して、王様に会った", "探して、勇者の泉に行った", "見つけた"]
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
  BIroExp = format(roExp, "020b")
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
             BIroExp[0:4]      + "0000"+ \
             "0"
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