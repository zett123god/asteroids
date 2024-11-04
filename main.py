import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return
       
        screen.fill(000)
        player.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
     
    
if __name__ == "__main__":
    main()
