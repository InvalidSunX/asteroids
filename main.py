import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = (clock.tick(60) / 1000)
    while 0 < 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=0)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()