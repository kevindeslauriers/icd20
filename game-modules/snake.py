import random
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
def main():
    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Snake properties
    snake_length = 1
    snake_positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # Food position
    food_pos = (random.randint(0, GRID_WIDTH-1) * BLOCK_SIZE, random.randint(0, GRID_HEIGHT-1) * BLOCK_SIZE)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT:
                    snake_direction = RIGHT

        # Move the snake
        #snake_positions[0][0] is the head x coordinate
        #snake_positions[0][1] is the head y coordinate
        # let's move the head
                    
        new_head = ((snake_positions[0][0] + snake_direction[0] * BLOCK_SIZE) % SCREEN_WIDTH,
                    (snake_positions[0][1] + snake_direction[1] * BLOCK_SIZE) % SCREEN_HEIGHT)

        # add the new head to the body
        snake_positions.insert(0, new_head) 

        # Check if snake eats food
        if snake_positions[0] == food_pos:
            snake_length += 1
            food_pos = (random.randint(0, GRID_WIDTH - 1) * BLOCK_SIZE,
                        random.randint(0, GRID_HEIGHT - 1) * BLOCK_SIZE)
        else:
            snake_positions.pop() # remember we added the head to make it bigger but if we don't eat food the snake should
                                # not be bigger so we remove the last piece - this is how we move

        # Fill the screen with white color
        screen.fill(WHITE)

        # Draw the snake
        for position in snake_positions:
            pygame.draw.rect(screen, RED, (position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw the food
        pygame.draw.rect(screen, BLACK, (food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(10)

    # Quit Pygame
    pygame.quit()


main()
