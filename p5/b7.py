l1=list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわがぎぐげござじずぜぞばびぶべぼぱぴぷぺぽ")
l2=list("０１２３４５６７８９あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんっゃゅょ゛゜　")
def f1(pa,pb):return format(pb.index(pa),"06b")
def f2(pa):return[pa[i:i+8].ljust(8,'0')for i in range(0,len(pa),8)]
def f3(pa):
    b=len(pa)*257
    for i in reversed(range(len(pa))):
        a=int(pa[i],2)
        for _ in range(8):
            if((b>>8)^a)&128:b=((b<<1)^4129)&0xFFFF
            else:b=(b<<1)&0xFFFF
            a=(a<<1)&0xFF
    return format(b&2047,"11b")
def f4(pa):return'\n'.join(['  '.join([pa[i:i+3],pa[i+3:i+6],pa[i+6:i+9]])for i in range(0,len(pa),10)])
a1=[f1(i,l2)for i in"０"*4]
a3=f2("0"*8+a1[2]+a1[1][:2]+"0"*8+a1[1][3:5]+a1[0]+"0"*8+a1[1][5]+a1[3]+a1[1][2]+"0"*50)
a4=f3(a3)
a3[0]=a4[6:]+a3[0][5:]
a3[8]=a3[8][:2]+a4[:6]
a5=''.join(a3)
a6=a5+'0'*((6-len(a5)%6)%6)
a7=[a6[i:i+6]for i in range(0,len(a6),6)]
for i in range(1,len(a7)):a7[i]=format((int(a7[i],2)+int(a7[i-2],2)+int(a7[0][3:5],2)+1)&63,"6b")
print(f4(''.join([l1[int(x,2)]for x in a7])))
