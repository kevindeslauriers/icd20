import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RGB Colors Example")

# Define RGB colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)

# Main loop
while True:
    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Draw colored rectangles
    pygame.draw.rect(screen, red, (50, 50, 100, 100))
    pygame.draw.rect(screen, green, (150, 50, 100, 100))
    pygame.draw.rect(screen, blue, (250, 50, 100, 100))
    pygame.draw.rect(screen, yellow, (50, 200, 100, 100))
    pygame.draw.rect(screen, magenta, (150, 200, 100, 100))
    pygame.draw.rect(screen, cyan, (250, 200, 100, 100))

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()