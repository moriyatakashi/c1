pl=list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞばびぶべぼぱぴぷぺぽ")
nl=list("０１２３４５６７８９あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんっゃゅょ゛゜　")
tb=lambda c,t:format(t.index(c),"06b")
s8=lambda s:[s[i:i+8].ljust(8,'0')for i in range(0,len(s),8)]
sh=lambda s:'\n'.join(['  '.join([s[i:i+3],s[i+3:i+6],s[i+6:i+9]])for i in range(0,len(s),10)])
def crc(c):
 r=len(c)*257
 for i in reversed(range(len(c))):
  o=int(c[i],2)
  for _ in range(8):
   r=((r<<1)^4129 if((r>>8)^o)&128 else r<<1)&65535
   o=(o<<1)&255
 return format(r&2047,"011b")
r="００００";e=g=0
bn=[tb(c,nl)for c in r]
re=format(e,"020b");re=re[4:]+re[:4]
s="00000000"+bn[2]+bn[1][:2]+format(g,"016b")[:8]+bn[1][3:5]+bn[0]+format(g,"016b")[8:]+bn[1][5]+bn[3]+bn[1][2]+"000000000000"+"00000"+"00000000"+re+"0000"+"0"
b=s8(s)
if len(b)==40:b[8]=b[39]
c=crc(b);b[0]=c[6:]+b[0][5:];b[8]=b[8][:2]+c[:6]
cm=''.join(b)+'0'*((6-len(''.join(b))%6)%6)
pw=[cm[i:i+6]for i in range(0,len(cm),6)]
shf=int(pw[0][3:5],2)+1
for i in range(1,len(pw)):pw[i]=format((int(pw[i],2)+int(pw[i-1],2)+shf)&63,"06b")
print(sh(''.join([pl[int(x,2)]for x in pw])))