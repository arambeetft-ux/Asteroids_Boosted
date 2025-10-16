import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)   

    All_asteroids = pygame.sprite.Group()
    Asteroid.containers = (All_asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    All_shots = pygame.sprite.Group()
    Shot.containers = (All_shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)

        for asteroid in All_asteroids:
            if player.Colision_Check(asteroid):
                print("Collision detected!")
                All_asteroids.remove(asteroid)
                drawable.remove(asteroid)
                updatable.remove(asteroid)
                print("Game Over!")
                return

        for asteroid in All_asteroids:
            for shot in All_shots:
                if shot.Colision_Check(asteroid):
                    print("Shot hit asteroid!")
                    All_asteroids.remove(asteroid)
                    drawable.remove(asteroid)
                    updatable.remove(asteroid)
                    All_shots.remove(shot)
                    drawable.remove(shot)
                    updatable.remove(shot)
                    if asteroid.radius > ASTEROID_MIN_RADIUS:
                        for _ in range(2):
                            new_asteroid = Asteroid(asteroid.position.x, asteroid.position.y, asteroid.radius - ASTEROID_MIN_RADIUS)
                            new_asteroid.velocity = asteroid.velocity.rotate(30 * (_ * 2 - 1))
                    break

        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()        
        clock.tick(60)        
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
    



if __name__ == "__main__":
    main()
