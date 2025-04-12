import pgzrun
import random

WIDTH = 1200
HEIGHT = 600
TITLE = "Gallaga Game!"

RED = "red"
BLACK = "black"

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

def draw():
    if lives > 0:
        screen.clear()
        screen.fill("blue")
        battleship.draw()
        for enemy in enemies:
            enemy.draw()
        for ball in cannonballs:
            ball.draw()
        display_score()
    else:
        game_over()

def game_over():
    is_game_over = True
    screen.clear()
    screen.fill("orange")
    screen.draw.text("Game MEOW OVER!",(WIDTH // 2 - 180,HEIGHT // 2 - 40),fontsize = 60,color = "White")
    screen.draw.text(f"meow!Final Score:{score}",(WIDTH // 2 - 180,HEIGHT // 2 + 15),fontsize = 45,color = "White")
    screen.draw.text("Press SPACE to play again!meow",(WIDTH // 2 - 180,HEIGHT // 2 + 60),fontsize = 45,color = "White")
    
    if keyboard.SPACE:
        restart_game()

def restart_game():
    global bullets, lives, score, enemies
    score = 0
    lives = 3
    cannonballs = []
    enemies = []
    for i in range(8):
        enemy = Actor("cat")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)

pgzrun.go()