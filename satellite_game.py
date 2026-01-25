import pgzrun
import random
from time import time
WIDTH=700
HEIGHT=550
satellites=[]
lines=[]
next_satellites=0
start_time=0
total_time=0
end_time=0
number_of_satellite=10

def create_satellites():
    global start_time
    for count in range(0,number_of_satellite):
        satellite=Actor('satellite')
        satellite.pos=random.randint(30,WIDTH-30),random.randint(30,HEIGHT-30)
        satellites.append(satellite)
    start_time=time()

def draw():
    global total_time
    screen.blit('space background',(0,0))
    number=1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
        number=number+1
    
    for line in lines:
        screen.draw.line(line[0],line[1],(255,0,0))
    if next_satellites < number_of_satellite:
        total_time=time()-start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    
def up_date():
    pass

def on_mouse_down(pos):
    global next_satellites
    global lines
    if next_satellites < number_of_satellite:
        if satellites[next_satellites].collidepoint(pos):
            if next_satellites:
                lines.appened((satellites[next_satellites-1].pos, satellites[next_satellites].pos))
                next_satellites+=1
        else:
            lines=[]
            next_satellites=0


create_satellites()



pgzrun.go()
