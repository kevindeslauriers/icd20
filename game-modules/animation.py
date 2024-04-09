import random
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_WIDTH = 823 // 6  # Width of a single sprite frame
SPRITE_HEIGHT = 547 // 4  # Height of a single sprite frame
NUM_ROWS = 4
NUM_COLS = 6

# Load sprite sheet image
sprite_sheet = pygame.image.load("spritesheet.png")

# Extract individual frames
sprite_frames = []
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        x = col * SPRITE_WIDTH
        y = row * SPRITE_HEIGHT
        sprite_frames.append(sprite_sheet.subsurface(pygame.Rect(x, y, SPRITE_WIDTH, SPRITE_HEIGHT)))

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Player position and movement
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Animation variables
current_animation = 0  # 0: down, 1: left, 2: right, 3: up
frame_index = 0
animation_speed = 0.2  # Seconds per frame

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill screen with white

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        current_animation = 1  # Set animation to left
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed
        current_animation = 2  # Set animation to right
    elif keys[pygame.K_UP]:
        player_y -= player_speed
        current_animation = 3  # Set animation to up
    elif keys[pygame.K_DOWN]:
        player_y += player_speed
        current_animation = 0  # Set animation to down

    # Display current frame
    screen.blit(sprite_frames[current_animation * NUM_COLS + int(frame_index)], (player_x, player_y))

    # Update frame index for animation
    frame_index += animation_speed
    if int(frame_index) >= NUM_COLS:
        frame_index = 0

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
sys.exit()
