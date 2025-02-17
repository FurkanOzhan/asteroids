# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
