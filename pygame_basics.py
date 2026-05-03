import pygame
WIDTH=500
HEIGHT=300
screen= pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,25,243))
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
