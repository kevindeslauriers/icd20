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
paddle_speed = 10
paddle1_x = 15
paddle1_y = SCREEN_HEIGHT // 2 - paddle_h //2

paddle2_x = SCREEN_WIDTH - 15 - paddle_w
paddle2_y = SCREEN_HEIGHT // 2 - paddle_h //2

ball_radius = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

ball_speed_x = 5
ball_speed_y = 5



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
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
        paddle1_y = max(paddle1_y, 0)  # Ensure player does not move off the left edge
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed
        paddle1_y = min(paddle1_y, SCREEN_HEIGHT - paddle_h)  # Ensure player does not move off the right edge
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
        paddle2_y = max(paddle2_y, 0)  # Ensure player does not move off the top edge
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed
        paddle2_y = min(paddle2_y, SCREEN_HEIGHT - paddle_h)  # Ensure player does not move off the bottom edge



    pygame.draw.rect(screen, BLACK, [paddle1_x, paddle1_y,paddle_w, paddle_h])
    pygame.draw.rect(screen, BLACK, [paddle2_x, paddle2_y,paddle_w, paddle_h])
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), ball_radius)

    clock.tick(60)  # Set the frame rate to 60 frames per second

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)
    paddle1_rect = pygame.Rect(paddle1_x, paddle1_y, paddle_w, paddle_h)
    paddle2_rect = pygame.Rect(paddle2_x, paddle2_y, paddle_w, paddle_h)



    if (ball_y + ball_radius> SCREEN_HEIGHT) or (ball_y - ball_radius < 0):
        ball_speed_y *= -1

    if (paddle1_rect.colliderect(ball_rect)) or (paddle2_rect.colliderect(ball_rect)):
        ball_speed_x *= -1

    # if (ball_x + ball_radius> SCREEN_WIDTH) :
    #     score1 += 1

    

    

    pygame.display.flip()


pygame.quit()
sys.exit()


