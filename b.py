def pl(p):
    p=p.rstrip()
    q=p.strip().split(maxsplit=2)
    a,b,c=(
        "", 
        q[0], 
        q[1]if len(q)>1 else""
    )if p.startswith(' ')else(
        q[0], 
        q[1]if len(q)>1 else"", 
        q[2]if len(q)>2 else""
    )
    if c.startswith("'")and c.endswith("'")and c:c=[c[1:-1]]
    else:c=[p.strip()for p in c.split(',')]if c else[]
    return{"label":a,"inst":b,"operands":c}
for p in open("a.txt"):print(pl(p))
