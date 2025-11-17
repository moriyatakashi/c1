from b import*

pa=[
    [58,60,62],
    [0,2,4],
    [6,8,10,12],
    [14,4,6],
    [8,10,12],
    [14,16]
]
# for ba in pa:
#     for bb in ba:
#         print(passDict[bb]+"("+f'{bb:06b}'+")",end="")
#     print()

for ba in pa:
    for bb in ba:
        print(f'{bb:06b}',end="")
    print()
