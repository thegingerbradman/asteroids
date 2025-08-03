import pygame
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT,
                       ASTEROID_MIN_RADIUS,
                       ASTEROID_KINDS,
                       ASTEROID_SPAWN_RATE,
                       ASTEROID_MAX_RADIUS)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
