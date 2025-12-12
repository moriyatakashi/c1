from caa import*
def droName():
  roName = "００００" 
  BIroName = [nameToBinary(char) for char in roName]
  return BIroName
def droItems():
  item_list = ["なし", "ひのきのぼう", "せいなるナイフ", "まどうしのつえ", "いかずちのつえ", "こんぼう", "どうのつるぎ", "くさりがま","てつのやり", "はやぶさのけん", "はがねのつるぎ", "おおかなずち", "はかいのつるぎ", "ドラゴンキラー", "ひかりのつるぎ","ロトのつるぎ", "いなずまのけん", "ぬののふく", "みかわしのふく", "みずのはごろも", "ミンクのコート", "かわのよろい","くさりかたびら", "あくまのよろい", "まほうのよろい", "はがねのよろい", "ガイアのよろい", "ロトのよろい", "かわのたて", "ちからのたて", "はがねのたて", "しにがみのたて", "ロトのたて", "ふしぎなかぶと", "てつかぶと", "ロトのかぶと", "ロトのしるし", "ふねのざいほう", "つきのかけら", "ルビスのまもり", "じゃしんのぞう", "せかいじゅのは", "やまびこのふえ", "ラーのかがみ","あまつゆのいと", "せいなるおりき", "かぜのマント", "あくまのしっぽ", "まよけのすず", "ふっかつのたま", "ゴールドカード", "ふくびきけん", "せいすい", "キメラのつばさ", "みみせん（使用不可）", "きんのかぎ","ぎんのかぎ", "ろうやのかぎ", "すいもんのかぎ", "どくけしそう", "やくそう", "いのりのゆびわ", "しのオルゴール（使用不可）","あぶないみずぎ（MSX専用）"]
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
  roItems = [item_list.index(i) for i in _roItems]
  roEquip = [1 if i else 0 for i in _roEquip]
  roItems, roEquip = remove_elements(roItems, roEquip)
  BIroItems = [format(equip, "01b") + format(item, "06b") for item, equip in zip(roItems, roEquip)]
  BIroItemsLen = format(len(roItems), "04b")
  return BIroItems,BIroItemsLen
def droExp():
  roExp = 0 
  gold = 0 
  pattern = 0 
  BIroExp = format(roExp, "020b")
  BIgold = format(gold, "016b")
  BIpattern = format(pattern, "04b")
  return BIroExp,BIgold,BIpattern
def dst():
  _town = "ローレシア" 
  _flagMoon = "使っていない" 
  _flagGate = "開けていない" 
  _flagPlumage = "織ってもらっていない" 
  _statShip = "何もしていない" 
  _statPrince = "見つけていない" 
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
  BItown = format(town, "03b")
  BIflagMoon = format(flagMoon, "01b")
  BIflagGate = format(flagGate, "01b")
  BIflagPlumage = format(flagPlumage, "01b")
  BIstatShip = format(statShip, "02b")
  BIstatPrince = format(statPrince, "02b")
  return BItown,BIflagMoon,BIflagGate,BIflagPlumage,BIstatShip,BIstatPrince
def dfla():
  _crestLife = False 
  _crestWater = False 
  _crestMoon = False 
  _crestStar = False 
  _crestSun = False 
  crestLife = 1 if _crestLife else 0
  crestWater = 1 if _crestWater else 0
  crestMoon = 1 if _crestMoon else 0
  crestStar = 1 if _crestStar else 0
  crestSun = 1 if _crestSun else 0
  BIcrestLife = format(crestLife, "01b")
  BIcrestWater = format(crestWater, "01b")
  BIcrestMoon = format(crestMoon, "01b")
  BIcrestStar = format(crestStar, "01b")
  BIcrestSun = format(crestSun, "01b")
  return BIcrestLife,BIcrestWater,BIcrestMoon,BIcrestStar,BIcrestSun
def b1():
  BIroName=droName()
  BIroItems,BIroItemsLen=droItems()
  BIroExp,BIgold,BIpattern=droExp()
  BItown,BIflagMoon,BIflagGate,BIflagPlumage,BIstatShip,BIstatPrince=dst()
  BIcrestLife,BIcrestWater,BIcrestMoon,BIcrestStar,BIcrestSun=dfla()
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
    "0"
  return bytes_str