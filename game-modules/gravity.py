import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame


# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define Ball properties
ball_radius = 20
ball_color = BLUE
ball_position = [screen_width // 2, 50]
ball_velocity = [0, 0]  # Initial velocity

# Define gravity
gravity = 0.1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Apply gravity
    ball_velocity[1] += gravity

    # Update ball position based on velocity
    ball_position[1] += ball_velocity[1]

    # Check for collision with floor
    if ball_position[1] + ball_radius >= screen_height:
        ball_position[1] = screen_height - ball_radius
        ball_velocity[1] *= -0.9  # Reverse velocity and dampen it on floor collision

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
