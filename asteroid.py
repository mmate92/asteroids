import pygame
import random
from logger import log_event

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        log_event("asteroid_split")
        rnd_angle = random.uniform(20, 50)
        first_new_astr_velocity = self.velocity.rotate(rnd_angle) * 1.2
        second_new_astr_velocity = self.velocity.rotate(rnd_angle*-1) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_new_asteroid.velocity = first_new_astr_velocity
        second_new_asteroid.velocity = second_new_astr_velocity



