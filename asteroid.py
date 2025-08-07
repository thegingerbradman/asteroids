import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt / 1000

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        baby1_velocity = self.velocity.rotate(random_angle)
        baby2_velocity = self.velocity.rotate(-random_angle)
        baby_radius = self.radius - ASTEROID_MIN_RADIUS
        baby1 = Asteroid(self.position[0], self.position[1], baby_radius)
        baby1.velocity = baby1_velocity * 1.2
        baby2 = Asteroid(self.position[0], self.position[1], baby_radius)
        baby2.velocity = baby2_velocity * 1.2
