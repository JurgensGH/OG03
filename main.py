import random

import pygame

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

color = (0, 0, 0)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, screen_width - target_width)
                target_y = random.randint(0, screen_height - target_height)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
