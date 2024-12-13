import pygame as pg
import math,random

pg.init()
W,H=800,600
scr=pg.display.set_mode((W,H))
pg.display.set_caption('Artillery Game')

class Tank:
    def __init__(s,x,p):
        s.x,s.y,s.p,s.a,s.p=x,0,p,45,50
    def draw(s):
        pg.draw.rect(scr,(0,255,0),(s.x-10,H-s.y-20,20,20))
        ex=s.x+math.cos(math.radians(s.a))*20
        ey=H-(s.y+math.sin(math.radians(s.a))*20)
        pg.draw.line(scr,(0,255,0),(s.x,H-s.y),((ex,ey)),4)

def gen_terrain():
    y=[random.randint(100,400)]
    for i in range(W-1):
        y.append(y[-1]+random.randint(-2,2))
        if y[-1]<100:y[-1]=100
        if y[-1]>400:y[-1]=400
    return y

class Explosion:
    def __init__(s,x,y):
        s.x,s.y,s.r,s.f=x,y,0,0
    def draw(s):
        s.r+=1
        s.f+=1
        pg.draw.circle(scr,(255,random.randint(0,255),0),(int(s.x),H-int(s.y)),s.r)
        return s.f>10

class Shell:
    def __init__(s,x,y,a,p):
        s.x,s.y=x,y
        s.vx=math.cos(math.radians(a))*p/2
        s.vy=math.sin(math.radians(a))*p/2
    def move(s,wind):
        s.x+=s.vx+wind
        s.y+=s.vy
        s.vy-=0.1
        return s.x<0 or s.x>W or s.y<0
    def draw(s):
        pg.draw.circle(scr,(255,0,0),(int(s.x),H-int(s.y)),2)

terr=gen_terrain()
p1=Tank(100,1)
p2=Tank(700,2)
plr,shell=1,None
wind=random.uniform(-0.5,0.5)
explosion=None

while 1:
    for e in pg.event.get():
        if e.type==pg.QUIT:exit()
        if e.type==pg.KEYDOWN and not shell:
            if e.key==pg.K_SPACE:
                t=p1 if plr==1 else p2
                shell=Shell(t.x,t.y,t.a,t.p)
                plr=3-plr
                wind=random.uniform(-0.5,0.5)
    
    if not shell:
        t=p1 if plr==1 else p2
        k=pg.key.get_pressed()
        if k[pg.K_LEFT]:t.a=min(90,t.a+1)
        if k[pg.K_RIGHT]:t.a=max(0,t.a-1)
        if k[pg.K_UP]:t.p=min(100,t.p+1)
        if k[pg.K_DOWN]:t.p=max(0,t.p-1)
    
    scr.fill((135,206,235))
    pg.draw.line(scr,(255,255,255),(10,30),(10+wind*50,30),3)
    for i in range(W-1):
        pg.draw.line(scr,(101,67,33),(i,H-terr[i]),(i+1,H-terr[i+1]))
    p1.draw()
    p2.draw()
    
    if shell:
        shell.draw()
        if shell.move(wind):
            explosion=Explosion(shell.x,shell.y)
            shell=None
    
    if explosion:
        if explosion.draw():
            explosion=None
    
    pg.display.flip()
    pg.time.Clock().tick(60)