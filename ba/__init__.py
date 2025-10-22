aa=[
    'A','B','C','D','E','F','G',
    'H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U',
    'V','W','X','Y','Z'
]
def ba3(pa):
    # 一文字目が文字であるか
    return True if pa[0]in aa else False
def ba4(pa):
    #二文字目が空文字であるか
    return True if pa[1]==' ' else False
def ba5(pa):
    #三文字目が文字であるか
    return True if pa[2]in aa else False
def ba6(pa):
    # 一文字目が文字であり、次が空文字であること
    0
    for pb in range(len(pa)):
        if pa[pb]==" ":break
    
