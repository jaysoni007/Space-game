import pygame

# Initialize Pygame
pygame.init()

# Create the Display Screen
screen = pygame.display.set_mode((800, 600))

# Create Player
playerImg = pygame.image.load("playerImg.png")
playerX = 350
playerY = 500
playerX_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

# Title and Icon
pygame.display.set_caption("Asteroids")
icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((150, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.1
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()
