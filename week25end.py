import pygame
import random

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

for i in range(60):
    sc = random.randint(0, 255)
    x_pos = random.randint(0, 800)
    y_pos = random.randint(0, 600)
    size = random.randint(10, 20)
    x_speed = random.randint(-3, 3)
    y_speed = random.randint(-3, 3)

    s = Square(x_pos, y_pos, size, x_speed, y_speed, (sc, sc, sc))
    allspriteslist.add(s)

pygame.init() # 0 s

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Snake Example')
clock = pygame.time.Clock()

background_colour = (0,0,0)


font = pygame.font.SysFont("comicsansms", 72)

start_time = pygame.time.get_ticks()
time_left = 30000
clicked_count = 0



done = False
while not done:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for sprite in allspriteslist:
                if sprite.rect.collidepoint(pos):
                    clicked_count = clicked_count + 1
                    sprite.remove(allspriteslist)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_b:
                background_colour = (0,0,200)
            if event.key == pygame.K_g:
                background_colour = (0,200,0)

    screen.fill(background_colour)

    remaining_time = (time_left-pygame.time.get_ticks()+start_time+500)//1000
    if remaining_time <= 0:
        remaining_time = 0
        over_text = font.render("Game Over", False, (0, 255, 0), (0, 0, 255))
        screen.blit(over_text, (200,300))
    else:
        allspriteslist.draw(screen)

    time = font.render(str(remaining_time), False, (0, 255, 0), (0, 0, 255))
    screen.blit(time, (100, 100))

    clicked_count_text = font.render(str(clicked_count), False, (0, 255, 0), (0, 0, 255))
    screen.blit(clicked_count_text, (300, 100))

    pygame.display.flip()
    allspriteslist.update()

    clock.tick(120)
pygame.quit()
