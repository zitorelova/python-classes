import pygame
import random
import pygame.gfxdraw

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.speed_x = -1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0,200,0))
        self.width = width

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        if self.rect.x < 0 - self.width:
            self.remove(obstacles)

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.fill((0,0,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([40,40], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movement = 0
        pygame.gfxdraw.filled_circle(self.image, 20, 20, 19, (237, 179, 19))

def check_collision(obstacles):
    for obstacle in obstacles:
        if bird.rect.colliderect(obstacle):
            return False
    
    if bird.rect.top < -40 or bird.rect.bottom >= 400:
            return False

    return True

def display_score():
    score_surface = game_font.render(str(int(score)), True, (255,255,255))
    score_rect = score_surface.get_rect(center=(400,200))
    screen.blit(score_surface, score_rect)

obstacles = pygame.sprite.Group()

last_obstacle_time = pygame.time.get_ticks() - 3000

ground_group = pygame.sprite.Group()
ground_group.add(Ground(0,400,800,200))

bird = Bird(100, 200)
gravity = 0.20

game_active = True
score = 0

pygame.init()

screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('comicsansms', 40)

done = False
while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == True:
                bird.movement = 0
                bird.movement -= 6
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                bird = Bird(100, 200)
                obstacles.empty()
                score = 0

    elapsed_time = pygame.time.get_ticks() - last_obstacle_time
    if elapsed_time > 3000:
        number = random.randint(-2, 2)
        obstacles.add(Obstacle(800, 220 - 30 * number, 50, 300))
        obstacles.add(Obstacle(800, 0, 50, 100 - 30 * number))
        last_obstacle_time = pygame.time.get_ticks()

    screen.fill((150,150,150))
    obstacles.draw(screen)
    ground_group.draw(screen)

    if game_active:
        bird.movement += gravity
        bird.rect.centery += bird.movement
        screen.blit(bird.image, bird.rect)
        game_active = check_collision(obstacles)

        obstacles.update()
        score += 0.01
        display_score()

        pygame.display.flip()
        clock.tick(120)

pygame.quit()
