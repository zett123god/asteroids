import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
                return
     screen.fill(000)
     pygame.display.flip()
    
if __name__ == "__main__":
    main()
