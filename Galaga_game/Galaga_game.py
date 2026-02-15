import pgzrun,random
WIDTH=700
HEIGHT=550
TITLE="Galaga Game"
BLUE=(0,0,255)
ship=Actor('galaga')
bug=Actor('bug')
ship.pos=(WIDTH//2,HEIGHT-60)
speed=20

bullets=[]
enemies=[]
enemies.append(bug)






pgzrun.go()
