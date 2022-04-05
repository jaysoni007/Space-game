import pygame

# Initialize Pygame
pygame.init()

# Create the Display Screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Asteroids")
icon = pygame.image.load('asteroid.png')
pygame.display.set_icon(icon)
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.update()
