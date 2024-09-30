import pygame
from pygame.examples.go_over_there import running

pygame.init()

running = True
while running:
    running = not running

pygame.quit()
