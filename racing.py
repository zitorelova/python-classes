import pygame

class Square(pygame.sprite.Sprite):
    
    def __init__(self, x, y, side, color):
        super().__init__()

        self.image = pygame.Surface([side, side], pygame.SRCALPHA)
        

pygame.init()

pygame.display.set_caption('Dump')
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 600])

done = False
while not done:
    print('try')

    screen.fill((150, 150, 150))

    pygame.display.flip()
    clock.tick(50)
pygame.quit()