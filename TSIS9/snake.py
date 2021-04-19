import pygame
import random
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((175, 134, 246))
pygame.display.set_caption('Snake')

class Food():
    def __init__(self, x=0, y=0, color=(255, 255, 255), width=16, height=16):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)


class Snake():
    def __init__(self):
        self.x = -1
        self.y = 50
        self.speed = 2
        self.velocity = [self.speed, 0]  # dx,dy
        self.size = 1
        self.radius = 8
        self.hitbox = pygame.Rect(
            self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)

        self.elements = [[self.x, self.y, self.hitbox]]

        self.up = False
        self.down = False
        self.right = True
        self.left = False

        for i in range(10):
            self.add_size()

    def add_size(self):
        self.size += 1
        self.hitbox = pygame.Rect(
            self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.elements.append([self.x, self.y, self.hitbox])

    def draw(self):
        for i in self.elements:
            
            self.hitbox = pygame.Rect(
                i[0]-self.radius, i[1]-self.radius, self.radius*2, self.radius*2)
            ind = self.elements.index(i)
            self.elements[ind][2] = self.hitbox
            pygame.draw.circle(screen, (148, 12, 100),
                               (i[0], i[1]), self.radius)

    def move(self):
        for i in range(1, self.size):
            self.elements[self.size-i][0] = self.elements[self.size-i-1][0]
            self.elements[self.size-i][1] = self.elements[self.size-i-1][1]
        self.elements[0][0] += self.velocity[0]
        self.elements[0][1] += self.velocity[1]


def spawn():
    while len(foods) < 8:
        x_ = random.randrange(64, 600, 10)
        y_ = random.randrange(64, 600, 32)
        color_ = (random.randrange(100, 255), random.randrange(
            100, 255), random.randrange(100, 255))
        width_ = height_ = random.randrange(8, 24, 4)
        foods.append(Food(x_, y_, color_, width_, height_))


def draw_score():
    global score
    font = pygame.font.SysFont('ComicSans', 24)
    text = font.render(f'Score:{score}', 1, (255, 255, 255))
    screen.blit(text, (500, 50))


def initializing():
    global score
    draw_score()
    snake.draw()
    snake.move()
    for f in foods:
        f.draw()
        if snake.elements[0][2].colliderect(f.hitbox):
            score += 1
            snake.add_size()
            foods.remove(f)


FPS = 60
clock = pygame.time.Clock()
level_num = 1
score = 0
walls = []
foods = []
snake = Snake()
run = True
while run:
    screen.fill((175, 134, 246))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(0, WIDTH, 10):
        pygame.draw.rect(screen, (255, 255, 12), (i, 0, 10, 10), 1)
        pygame.draw.rect(screen, (255, 255, 12), (i, WIDTH - 10, 10, 10), 1)
        pygame.draw.rect(screen, (175, 134, 246), (0, 50, 10, 10), 1)
        pygame.draw.rect(screen, (175, 134, 246), (0, 40, 10, 10), 1)
        pygame.draw.rect(screen, (255, 255, 12), (0, i , 10, 10), 1)
        pygame.draw.rect(screen, (255, 255, 12), (HEIGHT - 10, i, 10, 10), 1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and not snake.left:
        snake.right = True
        snake.up = snake.down = snake.left = False
        snake.velocity = [snake.speed, 0]
    elif keys[pygame.K_a] and not snake.right:
        snake.left = True
        snake.up = snake.down = snake.right = False
        snake.velocity = [-snake.speed, 0]
    elif keys[pygame.K_w] and not snake.down:
        snake.up = True
        snake.down = snake.right = snake.left = False
        snake.velocity = [0, -snake.speed]
    elif keys[pygame.K_s] and not snake.up:
        snake.down = True
        snake.up = snake.right = snake.left = False
        snake.velocity = [0, snake.speed]
    initializing()
    spawn()
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
