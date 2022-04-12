import pygame
import random
# Initialize Pygame
pygame.init()

# Create the Display Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('backgroundImg.png')

# Create Player
playerImg = pygame.image.load("playerImg.png")
playerX = 350
playerY = 500
playerX_change = 0

# Create Player
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Title and Icon
pygame.display.set_caption("Asteroids")
icon = pygame.image.load('asteroids.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Img
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -2.5
        if event.key == pygame.K_RIGHT:
            playerX_change = 2.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    player(playerX, playerY)

    enemy(enemyX, enemyY)

    pygame.display.update()
