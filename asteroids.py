from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            randAngle = random.uniform(20, 50)
            newVector1 = self.velocity.rotate(randAngle)
            newVector2 = self.velocity.rotate(-randAngle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            First = Asteroid(self.position[0], self.position[1], newRadius)
            Second = Asteroid(self.position[0], self.position[1], newRadius)
            First.velocity = newVector1 * 1.2
            Second.velocity = newVector2 * 1.2