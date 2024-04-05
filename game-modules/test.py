import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame


# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rotating Tetris Pieces')

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Block size
block_size = 20

# Define a function to draw a single block
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x, y, block_size, block_size))
    pygame.draw.rect(screen, WHITE, (x, y, block_size, block_size), 1)  # Border

# Tetris pieces rotation states
L_states = [
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 1), (1, 1), (2, 1), (0, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(2, 0), (0, 1), (1, 1), (2, 1)]
]

T_states = [
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 1), (2, 1), (1, 2)],
    [(1, 0), (1, 1), (2, 1), (1, 2)]
]

square_state = [
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]

# Function to draw pieces with rotation
def draw_piece(x, y, blocks, color, state):
    for block in blocks[state]:
        draw_block(x + block[0] * block_size, y + block[1] * block_size, color)

# Current rotation states
L_current_state = 0
T_current_state = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Rotate the pieces when 'R' is pressed
                L_current_state = (L_current_state + 1) % len(L_states)
                T_current_state = (T_current_state + 1) % len(T_states)

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Draw the Tetris pieces with rotation
    draw_piece(50, 50, L_states, BLUE, L_current_state)
    draw_piece(150, 50, T_states, RED, T_current_state)
    draw_piece(300, 50, square_state, YELLOW, 0)  # Square doesn't rotate

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
