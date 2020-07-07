import pygame
import random
import pygame.gfxdraw

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, side, speed_x, speed_y, colour):
        super().__init__()
        self.side = side
        self.image = pygame.Surface([side, side], pygame.SRCALPHA)

        self.speed_x=speed_x
        self.speed_y=speed_y

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.colour = colour
        # self.image.fill(colour)
        # pygame.draw.circle(self.image, (200,0,0), (side//2, side//2), int(side/2))
        pygame.gfxdraw.filled_circle(self.image, side//2, side//2, side//2-1, (200,0,0))


    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y

        # right
        if self.rect.x > 800 - self.side:
            self.rect.x = 800 - self.side
            self.speed_x = -self.speed_x

        # left
        if self.rect.x < 0:
            self.rect.x = 0
            self.speed_x = -self.speed_x

        # bar
        if self.rect.y > 580 - self.side and self.rect.y <= 590 - self.side:
            x, y = pygame.mouse.get_pos()
            if self.rect.x > x -130/2 - self.side and self.rect.x < x +130/2 :
                self.rect.y = 580 - self.side
                self.speed_y = -self.speed_y

        if self.rect.y > 600:
            self.remove(allspriteslist)

        # bottom        
        if self.rect.y < 0:
            self.rect.y = 0
            self.speed_y = -self.speed_y

allspriteslist = pygame.sprite.Group()

# for i in range(60):
def createBall():
    sc = random.randint(0, 255)

    # x_pos, y_pos = pygame.mouse.get_pos()

    x_pos = random.randint(0, 800)
    y_pos = 100

    x_speed = random.randint(-3, 3)
    y_speed = random.randint(1, 3)

    # x_pos = random.randint(0, 800)
    # y_pos = random.randint(0, 600)
    size = random.randint(5, 30)


    s = Ball(x_pos, y_pos, size, x_speed, y_speed, (sc, sc, sc))

    allspriteslist.add(s)

pygame.init() # 0 s

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Snake Example')
clock = pygame.time.Clock()

background_colour = (0,0,0)


font = pygame.font.SysFont("comicsansms", 72)


lasttime_balladd = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()
time_left = 1000000
clicked_count = 0

showIntro = True

done = False
while not done:

    for event in pygame.event.get():



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_b:
                background_colour = (0,0,200)
            if event.key == pygame.K_g:
                background_colour = (0,200,0)
            if event.key == pygame.K_SPACE and showIntro is True:
                showIntro = False
                start_time = pygame.time.get_ticks()


    screen.fill(background_colour)

    timer = (pygame.time.get_ticks()-start_time)//1000

    # intro screen
    if showIntro is True:
        intro_text = font.render("Welcome", False, (0, 255, 0))
        screen.blit(intro_text, (100, 100))

    # game playing
    elif True:

        if pygame.time.get_ticks()-lasttime_balladd > 10000:
            createBall()
            lasttime_balladd = pygame.time.get_ticks()

        allspriteslist.draw(screen)

        # print(allspriteslist.sprites())

        timer = font.render(str(timer), False, (0, 255, 0), (0, 0, 255))
        screen.blit(timer, (100, 100))

        clicked_count_text = font.render(str(clicked_count), False, (0, 255, 0), (0, 0, 255))
        screen.blit(clicked_count_text, (300, 100))

    # game over
    else:
        timer = 0
        over_text = font.render("Game Over", False, (0, 255, 0), (0, 0, 255))
        screen.blit(over_text, (200,300))
        allspriteslist.empty()


    x, y = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (255, 255, 255), (x-130/2, 580, 130, 10))

    pygame.draw.line(screen, (255,255,255), (x-130/2, 0), (x-130/2, 800), 1)
    pygame.draw.line(screen, (255,255,255), (x+130/2, 0), (x+130/2, 800), 1)



    pygame.display.flip()
    allspriteslist.update()

    clock.tick(120)
pygame.quit()
