import pygame as p,math as m,random as r
W=800;H=600;p.init();s=p.display.set_mode((W,H));d=p.display
class T:
 def __init__(s,x):s.x,s.y,s.a,s.p=x,0,45,50
 def d(s):
  p.draw.rect(s,(0,255,0),(s.x-10,H-20,20,20));e=s.x+m.cos(m.radians(s.a))*20;f=H-m.sin(m.radians(s.a))*20;p.draw.line(s,(0,255,0),(s.x,H),(e,f),4)
class B:
 def __init__(s,x,y,a,w):s.x,s.y=x,y;s.v=m.cos(m.radians(a))*25;s.u=m.sin(m.radians(a))*25;s.w=w
 def m(s):s.x+=s.v+s.w;s.y+=s.u;s.u-=.5;return s.x<0 or s.x>W or s.y<0
def r():
 global t,c,b,w,g;t=[T(50),T(750)];c=0;b=None;w=r.random()-.5;g=[r.randint(100,400)]+[min(400,max(100,g[-1]+r.randint(-2,2)))for _ in range(W-1)]
r()
while 1:
 for e in p.event.get():
  if e.type==12:exit()
  if e.type==p.KEYDOWN and e.key==32 and not b:b=B(t[c].x,0,t[c].a,w);c=1-c;w=r.random()-.5
 if not b:k=p.key.get_pressed();d=t[c];k[p.K_LEFT]and(setattr(d,'a',min(90,d.a+1)));k[p.K_RIGHT]and(setattr(d,'a',max(0,d.a-1)));k[p.K_UP]and(setattr(d,'p',min(100,d.p+1)));k[p.K_DOWN]and(setattr(d,'p',max(0,d.p-1)))
 s.fill((135,206,235));[p.draw.line(s,(101,67,33),(i,H-g[i]),(i+1,H-g[i+1]))for i in range(W-1)];[t.d()for t in t]
 b and(p.draw.circle(s,(255,0,0),(int(b.x),H-int(b.y)),2),b.m()and(b:=None))
 document.getElementById('w').textContent=f'Wind: {w:.2f}';d.flip();p.time.Clock().tick(60)