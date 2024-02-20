# Simple pygame program

# Import and initialize the pygame library
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1280, 720])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 50, 50))
    # pygame.draw.circle(screen, (0, 255, 0), (400, 300), 30)
    # pygame.draw.line(screen, (0, 0, 255), (0, 0), (800, 600), 2)
    # pygame.draw.polygon(screen, (255, 255, 0), [(200, 200), (300, 300), (400, 200)])
    # pygame.draw.arc(screen, (255, 0, 255), pygame.Rect(100, 100, 200, 200), 0, 3.14, 2)
    # pygame.draw.ellipse(screen, (0, 0, 255), pygame.Rect(200, 200, 200, 100))
    # pygame.draw.aaline(screen, (255, 0, 255), (0, 0), (800, 600))
    # pygame.draw.lines(screen, (100, 255, 0), False, [(100, 100), (200, 200), (300, 100)], 2)









    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()