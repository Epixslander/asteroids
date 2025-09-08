import pygame
from constants import *


def main():
    play_game = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while play_game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
                return

        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        play_game = True





if __name__ == "__main__":
    main()
