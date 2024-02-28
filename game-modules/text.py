import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame



# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create a font object
font = pygame.font.SysFont(None, 48)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw text to the screen
    text = font.render("Hello, Pygame @ (25, 25)!", True, BLACK)
    screen.blit(text, (25,25))

    text2 = font.render("I am centered", True, BLACK)
    text_rect = text2.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(text2, text_rect)


    # Refresh screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
