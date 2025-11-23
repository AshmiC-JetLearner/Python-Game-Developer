import pgzrun, random
WIDTH=600
HEIGHT=600
def draw():
    r=random.randint(0,255)
    g=0
    b=255
    width=WIDTH-200
    height=HEIGHT-200
    for i in range(32):
        rect=Rect((0,0),(width,height))
        rect.center=(150,150)
        screen.draw.rect(rect,(r,g,b))
        b=b-8
        g=g+8
        width=width-10
        height=height-10

pgzrun.go()
