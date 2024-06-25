import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-50, 0)
        self.speed = random.randint(2, 5)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 2, 10))

def main():
    clock = pygame.time.Clock()
    raindrops = [Raindrop() for _ in range(200)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for raindrop in raindrops:
            raindrop.move()
            raindrop.draw()

            if raindrop.y > HEIGHT:
                raindrop.y = random.randint(-50, 0)
                raindrop.x = random.randint(0, WIDTH)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()