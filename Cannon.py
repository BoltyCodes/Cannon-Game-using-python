from turtle import *
from random import randrange
from freegames import vector

ball=vector(-200,-200)
speed=vector(0,0)
target=[]

def tap(x,y):
  if not inside(ball):
    ball.x=-199
    ball.y=-199
    speed.x=(x+400)/25
    speed.y=(y+400)/25

def inside(xy):
  return -200<xy.x<200 and -200<xy.y<200

def draw():
  clear()
  for t in target:
    goto(t.x,t.y)
    dot(20,"blue")
    
    inside(ball)

    goto(ball.x,ball.y)
    dot(20,"red")
 

def move():
  if randrange(40)==0:
    y=randrange(-50,50)
    t=vector(200,y)
    target.append(t)

  for t in target:
    t.x -=0.5
  
  if inside(ball):
    speed.y -= 0.35
    ball.move(speed)

  dupe=target.copy()
  target.clear()

  for t in dupe:
 
    if abs(t-ball)>13:
      target.append(t)
  draw()


   
  ontimer(move,50)

setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
inside()
