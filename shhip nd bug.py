import pgzrun

import random
WIDTH = 1200
HEIGHT=600
BLACK = (0,0,0)
LIMEGREEN = (50,205,50)
ship = Actor('spaceship')
bug = Actor('bug')
ship.pos =(WIDTH//3,HEIGHT-60)
score=0
speed=5
bullets = []

enemies = []
enemies.append(Actor('bug'))
enemies[-1].x = 10

enemies[-1].y = -100
def displayScore():
    screen.draw.text(str(score),(50,30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.apprnd(Actor('bullet'))
        bullets[-1].x =ship.x
        bullets[-1].y-50

def update():
    global score
    if keyboard.left:
        ship.x-=speed
        if ship.x <=0:
            ship.x = 0

    elif keyboard.right:
        ship.x += speed
        if ship.x>=WIDTH:
            ship.x = WIDTH

    for bullet in bullets:
        if bullets.y<=0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    for enemy in enemies:
        enemy.y +=5

        if enemy.y>=HEIGHT:
            enemy.y = -100
            enemy.x=random.randint(50,WIDTH-50)

        for bullet in bullets:
            if enemy.colliderect(bullet):
               score +=100

               bullets.remove(bullet)
               enemies.remove(enemy)

def draw():
    screen.clear()
    screen.fill(LIMEGREEN)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    ship.draw()
    displayScore

pgzrun.go()
