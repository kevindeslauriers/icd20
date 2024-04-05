import random
import sys
sys.path.append('C:\\Python312\\Lib\\site-packages')

import pygame
import os

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Catcher")

circles = []

# Function to create new circles
def create_circle(x,y):
    radius = 10
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    circle = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius}
    circles.append(circle)


create_circle(50, 10)
create_circle(10, 10)

circle = random.choice(circles)

# start loop now

