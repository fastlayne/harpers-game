import pygame as p,math as m,random as r,time as t
W=800;H=600;p.init();s=p.display.set_mode((W,H));d=p.display
class T:
 def __init__(s,x):s.x,s.y,s.a,s.p,s.h=x,0,45,50,100
 def d(s):
  p.draw.rect(s,(0,99,0),(s.x-10,H-20,20,20));e=s.x+m.cos(m.radians(s.a))*20;f=H-m.sin(m.radians(s.a))*20;p.draw.line(s,(0,99,0),(s.x,H),(e,f),4);p.draw.rect(s,(255,0,0),(s.x-10,H-35,20*s.h/100,5))
class B:
 def __init__(s,x,y,a,w,p):s.x,s.y=x,y;v=p/2;s.v=m.cos(m.radians(a))*v;s.u=m.sin(m.radians(a))*v;s.w=w
 def m(s):s.x+=s.v+s.w;s.y+=s.u;s.u-=.5;return[s.x,s.y,s.x<0or s.x>W or s.y<0]
class E:
 def __init__(s,x,y):s.x,s.y,s.r,s.f=x,y,0,0
 def d(s):s.r+=2;s.f+=1;[p.draw.circle(s,(255,r.randint(0,255),0),(int(s.x),H-int(s.y)),s.r-i)for i in range(3)];return s.f>8
def r():
 global t,c,b,w,g,e,l;t=[T(50),T(750)];c=0;b=None;w=r.random()-.5;g=[r.randint(100,400)]+[min(400,max(100,g[-1]+r.randint(-2,2)))for _ in range(W-1)];e=None;l=None
r()
while 1:
 for v in p.event.get():
  if v.type==12:exit()
  if v.type==p.KEYDOWN and v.key==32 and not b and not e:b=B(t[c].x,0,t[c].a,w,t[c].p);c=1-c;w=r.random()-.5
 if not b and not e:k=p.key.get_pressed();o=t[c];k[p.K_LEFT]and(setattr(o,'a',min(90,o.a+1)));k[p.K_RIGHT]and(setattr(o,'a',max(0,o.a-1)));k[p.K_UP]and(setattr(o,'p',min(100,o.p+1)));k[p.K_DOWN]and(setattr(o,'p',max(0,o.p-1)))
 s.fill((135,206,235));[p.draw.line(s,(101,67,33),(i,H-g[i]),(i+1,H-g[i+1]))for i in range(W-1)];[q.d()for q in t]
 if b:
  x,y,f=b.m();p.draw.circle(s,(255,0,0),(int(x),H-int(y)),2)
  if f:e=E(x,y);b=None
  for i,q in enumerate(t):h=abs(q.x-x);(h<20)and(q.h:=max(0,q.h-25))and(q.h<1)and(l:=f'P{2-i} Wins!')
 if e:e.d()and(e:=None)
 l and p.draw.rect(s,(0,0,0),(W//2-40,H//2-15,80,30))and p.draw.text(p.font.Font(None,30).render(l,1,(255,255,255)),(W//2-35,H//2-10))
 document.getElementById('w').textContent=f'Wind: {w:.2f}';d.flip();p.time.Clock().tick(60)