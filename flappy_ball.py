import pgzrun
from random import randint
TITLE='Flappy Ball'
WIDTH=600
HEIGHT=650
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
color=(r,g,b)

gravity=2000.0

class ball:
    def __init__(self,initial_x,initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=80

    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,color)

#creating object
ball1=ball(50,90)
def draw():
    screen.clear()
    ball1.draw()


def update(dt):
    uy=ball1.vy 
    ball1.vy += gravity*dt
    ball1 += (uy+ball1.vy)*0.5*dt

    #handle and detect the bounce
    if ball1.y > HEIGHT- ball1.radius:
        ball1.y = HEIGHT-ball1.radius
        ball1.vy = -ball1.vy*0.9

    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH-50 or ball1.x < 50:
        ball1.vx = -ball1.vx

def on_key_down(key):
    if key==keys.SPACE:
        ball1.vy =-900





pgzrun.go()
