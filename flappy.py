import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.speed_x = -1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((200,0,0))

    def update(self):
        self.rect.x = self.rect.x + self.speed_x

obstacles = pygame.sprite.Group()
obstacles.add(Obstacle(700, 220, 50, 300))

pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

done = False
while not done:
    
    obstacles.draw(screen)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
