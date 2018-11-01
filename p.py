#Q1

import pygame
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Question 1")
clock=pygame.time.Clock()
running=True
b=0
g=0
r=255
rdic=1

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    pygame.draw.circle(screen,(r,g,b),(400,300),100)
    pygame.display.update()
    clock.tick(60)
    print(r)
    if r>=255 or r<=0:
        rdic=-rdic

    r+=rdic

pygame.quit

#Q3
import pygame
import random
screen_2=pygame.display.set_mode((800,600))
pygame.display.set_caption("question 3")
running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    for i in range(0,30):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        pygame.draw.circle(screen_2,(r,g,b),(400,300),300-10*i)
        pygame.display.update()


pygame.quit()

#Q5
import pygame
import math
import random
clock=pygame.time.Clock()
screen_3=pygame.display.set_mode((800,600))
pygame.display.set_caption("Question 5/collision detection")
running=True
r_1=80
r_2=100

x=50
x_velocity=2
y=250
y_velocity=2

x_2=50
x_2_velocity=2
y_2=200
y_2_velocity=2
distance=math.hypot(x-x_2,y-y_2)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen_3.fill((0,0,0))
    pygame.draw.circle(screen_3,(255,0,0),(int(x),int(y)),r_1)
    pygame.draw.circle(screen_3, (255, 0, 0), (int(x_2), int(y_2)),r_2)

    pygame.display.flip()
    clock.tick(40)
    x=x+x_velocity
    y=y+y_velocity
    x_2+=x_2_velocity
    y_2+=y_2_velocity
    if x>590 or x<50:
        x_velocity=-x_velocity
    if y>430 or y<50:
        y_velocity=-y_velocity

    if x_2>590 or x_2<50:
        x_2_velocity=-x_2_velocity
    if y>300 or y<50:
        y_2_velocity = -y_2_velocity

   








pygame.quit()










