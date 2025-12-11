from dqa import*
def a1():
    pa={}
    for i in range(64):
        pa[passDict[i]]=i
    return pa
def a2(qa):
    pa=a1()
    pb=[]
    for i in range(18):
        pb+=[pa[qa[i]]]
    return pb
def a3(pa):
    pb=[pa[0]]
    for i in range(1,18):
        pb+=[(pa[i]-pa[i-1]-2)%64]
    return pb