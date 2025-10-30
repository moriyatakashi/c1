import pygame as p
import math as m
p.init()
s=p.display.set_mode((640,480))
c=p.time.Clock()
a=0
while 1:
    for e in p.event.get():
        if e.type==p.QUIT:exit()
    s.fill((0,0,0))
    r=[[x*m.cos(a)-z*m.sin(a),y,x*m.sin(a)+z*m.cos(a)]for x,y,z in[[0,1,0],[-1,-1,-1],[1,-1,-1],[0,-1,1]]]
    q=[(320+x*200/(z+5),240-y*200/(z+5))for x,y,z in r]
    for i,j,k in[(0,1,2),(0,2,3),(0,3,1),(1,2,3)]:
        u=[r[j][n]-r[i][n]for n in range(3)]
        w=[r[k][n]-r[i][n]for n in range(3)]
        n=[u[1]*w[2]-u[2]*w[1],u[2]*w[0]-u[0]*w[2],u[0]*w[1]-u[1]*w[0]]
        p.draw.polygon(s,[int(255*max(0,n[2]/(m.sqrt(sum(x*x for x in n))+1e-6)))]*3,[q[i],q[j],q[k]])
    p.display.flip()
    a+=0.02
    c.tick(30)