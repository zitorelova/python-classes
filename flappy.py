import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.speed_x = -1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0,200,0))

    def update(self):
        self.rect.x = self.rect.x + self.speed_x

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill((0,0,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

obstacles = pygame.sprite.Group()

for i in range(11):
    number = random.randint(-2, 2)
    obstacles.add(Obstacle(700 + i * 140, 220 - 30 * number, 50, 300))
    obstacles.add(Obstacle(700 + i * 140, 0, 50, 100 - 30 * number))

ground_group = pygame.sprite.Group()
ground_group.add(Ground(0,400,800,200))

pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

done = False
while not done:
    
    screen.fill((150,150,150))
    obstacles.draw(screen)
    ground_group.draw(screen)

    obstacles.update()

    pygame.display.flip()
    clock.tick(120)
pygame.quit()
