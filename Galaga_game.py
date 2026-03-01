import pgzrun, random
WIDTH=700
HEIGHT=600
TITLE="Galaga game"
BLUE=(0,0,255)

ship=Actor('ship')
bug=Actor('enemy')
ship.pos(WIDTH//2,HEIGHT-50)
speed=20

bullets=[]
enemies=[]

enemies.append(Actor('enemy'))
enemies[-1].x=100
enemies[-1].y=-100
score=0


def display_score():
    screen.draw.text(str(score),(100,30),fontsize=40)

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50

def update():
    pass

def draw():
    pass

pgzrun.go()
