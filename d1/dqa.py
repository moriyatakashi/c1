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
from aaa import*
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
             BIsaFlag
bytes_str=ba2(ba1(),bytes_str)
jumon=aa1(bytes_str)
aaa(jumon,"a1.json")
aab("b1.json")
