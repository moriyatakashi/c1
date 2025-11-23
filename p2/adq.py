passDict={0:"あ",1:"い",2:"う",3:"え",4:"お",5:"か",6:"き",7:"く",8:"け",9:"こ",
  10:"さ",11:"し",12:"す",13:"せ",14:"そ",15:"た",16:"ち",17:"つ",18:"て",19:"と",
  20:"な",21:"に",22:"ぬ",23:"ね",24:"の",25:"は",26:"ひ",27:"ふ",28:"へ",29:"ほ",
  30:"ま",31:"み",32:"む",33:"め",34:"も",35:"や",36:"ゆ",37:"よ",38:"ら",39:"り",
  40:"る",41:"れ",42:"ろ",43:"わ",44:"が",45:"ぎ",46:"ぐ",47:"げ",48:"ご",49:"ざ",
  50:"じ",51:"ず",52:"ぜ",53:"ぞ",54:"ば",55:"び",56:"ぶ",57:"べ",58:"ぼ",59:"ぱ",
  60:"ぴ",61:"ぷ",62:"ぺ",63:"ぽ"}
bytes=[("0"*97)[i:i+8]for i in range(0,97,8)]
if len(bytes[-1])<8:bytes[-1]=bytes[-1].ljust(8,'0')
crc=len(bytes)*0x0101
for i in range(len(bytes)-1,-1,-1):
  octed=int(bytes[i],2)  
  for j in range(8):
    carry_bit=((crc>>8)^octed)&0x80!=0
    crc=(crc<<1)&0xffff
    octed=(octed<<1)&0xff
    if carry_bit:crc^=0x1021
crc=format(crc&0x07ff,"011b")
bytes[0]=crc[6:]+bytes[0][5:]
bytes[8]=bytes[8][:2]+crc[:6]
combined_str=''.join(bytes)
remainder=len(combined_str)%6
if remainder>0:combined_str+='0'*(6-remainder)
password=[combined_str[i:i+6]for i in range(0,len(combined_str),6)]
nShift=int(password[0][3:5],2)+1
for i in range(1,len(password)):password[i]=format(((int(password[i],2)+int(password[i-1],2)+nShift)&0x3f),"06b")
jumon=""
passTemp=password.copy()
for i in range(len(password)):jumon+=passDict[int(passTemp.pop(0),2)]
print(crc)
print(password)
print(jumon)
