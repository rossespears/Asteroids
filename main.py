# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroidSwarm = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    print("Starting asteroids!")
    print (f"Screen width:",  SCREEN_WIDTH)
    print (f"Screen height:", SCREEN_HEIGHT)    
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroidSwarm, updateables, drawables)
    AsteroidField.containers = (updateables)
    shot.containers = (shots, updateables, drawables)
    field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateables.update(dt)
        for asteroid in asteroidSwarm:
            if(asteroid.collide(player1)):
                print("Game Over")
                sys.exit()
            for bullet in shots:
                if(asteroid.collide(bullet)):
                    asteroid.split()
        #drawables.draw(screen)
        for drawing in drawables:
            drawing.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()