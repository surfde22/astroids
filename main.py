# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for shape in updatable:
            shape.update(dt)
        
        screen.fill("black")
        
        for shape in drawable:
            shape.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()