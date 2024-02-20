import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Rectangle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle properties
rect_width, rect_height = 50, 50
rect_x, rect_y = WIDTH // 2 - rect_width // 2, HEIGHT // 2 - rect_height // 2
rect_speed = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Ensure the rectangle stays within the screen boundaries
    rect_x = max(0, min(WIDTH - rect_width, rect_x))
    rect_y = max(0, min(HEIGHT - rect_height, rect_y))

    # Draw to the screen
    screen.fill(WHITE)  # Fill the screen with white
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))  # Draw the rectangle

    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
