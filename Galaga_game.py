import pgzrun, random
WIDTH=700
HEIGHT=600
TITLE="Galaga game"
BLUE=(0,0,255)

ship=Actor('ship')
bug=Actor('enemy')
ship.pos=(WIDTH//2,HEIGHT-50)
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
    global score
    #to make the ship move left
    if keyboard.left:
        ship.x=ship.x-10
        if ship.x <= 0:
            ship.x = 0

    #to make the ship move right
    elif keyboard.right:
        ship.x += 10
        if ship.x >= WIDTH:
            ship.x = WIDTH

    #to fire bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    for enemy in enemies:
        enemy.y += 5
        if enemy.y >= HEIGHT:
            enemy.y= -100
            enemy.x=random.randint(10,WIDTH-10)
        
        #checking for the collision
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)



def draw():
    screen.clear()
    screen.fill(BLUE)
    
    for bullet in bullets:
        bullet.draw()
        
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    display_score()




pgzrun.go()
