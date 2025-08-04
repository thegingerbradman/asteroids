import pygame
from constants import(SCREEN_WIDTH, SCREEN_HEIGHT,
                      ASTEROID_MIN_RADIUS,
                      ASTEROID_KINDS,
                      ASTEROID_SPAWN_RATE,
                      ASTEROID_MAX_RADIUS)
from player import Player
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        dt = clock.tick(60)
        player.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
