import pygame
import random
import sys


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, side, speed_x, speed_y, colour):
        super().__init__()
        self.side = side
        self.image = pygame.Surface([side, side])

        self.speed_x=speed_x
        self.speed_y=speed_y


        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.colour = colour
        self.image.fill(colour)

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y

        if self.rect.x > 800:
            self.rect.x = -self.side
        if self.rect.x < -self.side:
            self.rect.x = 800
        if self.rect.y > 600:
            self.rect.y = -self.side

        if self.rect.y < -self.side:
            self.rect.y = 600
allspriteslist = pygame.sprite.Group()

for i in range(100):
    s = Square(i*30, i*40, 20,random.randint(-10,10),random.randint(-10,10),(random.randint(150, 255), 0, 0))
    allspriteslist.add(s)

my_square = Square(300, 200, 40, 0, 0, (random.randint(100, 255), 100, 0))
allspriteslist.add(my_square)


pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Snake Example')
clock = pygame.time.Clock()

background_colour = (0,0,0)
done = False
while not done:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for sprite in allspriteslist:
                if sprite.rect.collidepoint(pos):
                    sprite.remove(allspriteslist)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_b:
                background_colour = (0,0,200)
            if event.key == pygame.K_g:
                background_colour = (0,200,0)

    screen.fill(background_colour)
    allspriteslist.draw(screen)
    pygame.display.flip()
    allspriteslist.update()

    clock.tick(120)
pygame.quit()