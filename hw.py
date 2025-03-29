import pgzrun
import random

WIDTH = 1200
HEIGHT = 600
TITLE = "Gallaga Game!"

RED = "red"
BLACK = "black"

# Create the player
battleship = Actor("battleship")
battleship.pos = (WIDTH / 2,HEIGHT - 60)

is_game_over = False
cannonballs = []
score = 0
lives = 3
enemies = []
for i in range(8):
    enemy = Actor("cat")
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

speed = 5

def display_score():
    screen.draw.text(f"Score: {score}",(50,30))
    screen.draw.text(f"Lives: {lives}",(50,60))


def on_key_down(key):
    if key == keys.SPACE:
        ball = Actor("cannonball")
        ball.x = battleship.x
        ball.y = battleship.y - 50
        cannonballs.append(ball)

def update():
    global score
    global lives
    

    if keyboard.left:
        battleship.x -= speed
        if battleship.x <= 0:
            battleship.x = 0
    if keyboard.right:
        battleship.x += speed
        if battleship.x >= WIDTH:
            battleship.x = WIDTH

    for ball in cannonballs:
        if ball.y <= 0:
            cannonballs.remove(ball)
        else:
            ball.y -= 10
    
    move_down = False
    for enemy in enemies:
        enemy.y += 5
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
        
        for ball in cannonballs:
            if enemy.colliderect(ball):
                sounds.meow.play()
                score += 100
                cannonballs.remove(ball)
                enemies.remove(enemy)

        if enemy.colliderect(battleship):
            lives -= 1
            enemies.remove(enemy)
            if lives == 0:
                game_over()

    if len(enemies) < 8:
        enemy = Actor("cat")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

pgzrun.go()