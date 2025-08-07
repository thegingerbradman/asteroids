import pygame
from constants import(SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS,
                      ASTEROID_KINDS, ASTEROID_SPAWN_RATE,
                      ASTEROID_MAX_RADIUS, PLAYER_SHOOT_COOLDOWN)
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Print game info
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game init
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteriods, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    AsteroidField()

    # Game loop
    while True:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        player.timer -= dt
        for asteroid in asteriods:
            if asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()

if __name__ == "__main__":
    main()
