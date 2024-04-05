import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define bowling ball properties
ball_radius = 20
ball_color = BLACK
ball_position = [screen_width // 4, screen_height - 50]  # Start position on the left side of the screen
ball_velocity = [0, 0]  # Initial velocity

# Define bowling pins properties
pin_radius = 10
pin_color = RED
pin_gap = 20  # Gap between pins
pin_row_count = 4  # Number of rows of pins
pin_positions = []

# Generate pin positions in a triangular formation on the right side of the screen
for row in range(pin_row_count):
    y = screen_height // 4 + row * (pin_radius * 4 + pin_gap)
    start_x = screen_width * 3 // 4 - row * (pin_radius * 2 + pin_gap)
    for i in range(row + 1):
        x = start_x + i * (pin_radius * 4 + pin_gap * 2)
        pin_positions.append((x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw bowling ball
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

    # Draw bowling pins
    for pin_position in pin_positions:
        pygame.draw.circle(screen, pin_color, pin_position, pin_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()