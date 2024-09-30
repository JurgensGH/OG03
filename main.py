import pygame
from pygame.examples.go_over_there import running
import random
import time

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Shooting Gallery")
icon = pygame.image.load("image/icon.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("image/target.png")
target_width = 50
target_height = 50
target_x = random.randint(0, screen_width - target_width)
target_y = random.randint(0, screen_height - target_height)

color = (355, 355, 355)

running = True
while running:
    pass

pygame.quit()
