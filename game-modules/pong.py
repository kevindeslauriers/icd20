import random
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')

import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")


paddle_w = 20
paddle_h = 80
paddle1_x = 15
paddle1_y = SCREEN_HEIGHT // 2 - paddle_h //2

paddle2_x = SCREEN_WIDTH - 15 - paddle_w
paddle2_y = SCREEN_HEIGHT // 2 - paddle_h //2


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, BLACK, [paddle1_x, paddle1_y,paddle_w, paddle_h])
    pygame.draw.rect(screen, BLACK, [paddle2_x, paddle2_y,paddle_w, paddle_h])

    clock.tick(60)  # Set the frame rate to 60 frames per second

    pygame.display.flip()


pygame.quit()
sys.exit()


