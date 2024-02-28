import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')
import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_LENGTH = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_LENGTH))
pygame.display.set_caption("House Drawing")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
GRAY = (100,100,100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (300, 200, 200, 150)) 
    pygame.draw.polygon(screen, YELLOW, [(300, 200), (400, 100), (500, 200)])  
    pygame.draw.rect(screen, RED, (375, 280, 50, 70))
    pygame.draw.circle(screen, BLUE, (350, 230), 20)  
    pygame.draw.circle(screen, BLUE, (450, 230), 20) 
    pygame.draw.rect(screen, GREEN, (0, 350, 800, 750))  
    pygame.draw.rect(screen, BROWN, (70, 250, 40, 100)) 
    pygame.draw.polygon(screen, GREEN, [(0, 250), (100, 50), (200, 250)]) 
    pygame.draw.polygon(screen, GREEN, [(20, 200), (100, 50), (180, 200)])
    pygame.draw.polygon(screen, GREEN, [(40, 150), (100, 50), (160, 150)]) 
    pygame.draw.circle(screen, GRAY, (200, 55), 40)
    pygame.display.flip()

pygame.quit()