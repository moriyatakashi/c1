def c(p):
    b=3341
    for i in reversed(range(13)):
        a=int(p[i], 2)
        for _ in range(8):
            b=((b<<1)^4129 if((b>>8)^a)&128 else b<<1)&0xFFFF
            a=(a<<1)&0xFF
    return format(b&2047,"011b")
x=[("0"*98)[i:i+8].ljust(8,'0')for i in range(0,98,8)]
y=c(x)
print(y)
x[0]=y[6:]+x[0][5:]
x[8]=x[8][:2]+y[:6]
s="".join(x)+'0'*((6-len("".join(x))%6)%6)
z=[s[i:i+6]for i in range(0,len(s),6)]
print(*z)
for i in range(1,18):z[i]=format((int(z[i],2)+int(z[i-2],2)+int(z[0][3:5],2)+1)&63,"06b")
print(*z)
