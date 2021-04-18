import pygame
import random
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((175, 134, 246))
pygame.display.set_caption('Snake')


class Fruit():
    def __init__(self, x=-200, y=-200, color=(255, 255, 255), width=16, height=16):
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
        pygame.draw.rect(screen, [0, 255, 0],
                         (self.x, self.y, self.width, self.height), 1)


class Snake():
    def __init__(self):
        self.x = 128
        self.y = 128
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
        for element in self.elements:
            pygame.draw.circle(screen, ((
                3*element[0]) % 256, 100, (element[0]+element[1]) % 256), element[0:2], self.radius)
            self.hitbox = pygame.Rect(
                element[0]-self.radius, element[1]-self.radius, self.radius*2, self.radius*2)
            ind = self.elements.index(element)
            self.elements[ind][2] = self.hitbox
            pygame.draw.rect(screen, [255, 2, 255], (element[0]-self.radius,
                             element[1]-self.radius, self.radius*2, self.radius*2), 1)

    def move(self):
        for i in range(1, self.size):
            self.elements[self.size-i][0] = self.elements[self.size-i-1][0]
            self.elements[self.size-i][1] = self.elements[self.size-i-1][1]
        self.elements[0][0] += self.velocity[0]
        self.elements[0][1] += self.velocity[1]


def spawn_fruit():
    while len(fruits) < 8:
        x_ = random.randrange(64, 600, 10)
        y_ = random.randrange(64, 600, 32)
        color_ = (random.randrange(100, 255), random.randrange(
            100, 255), random.randrange(100, 255))
        width_ = height_ = random.randrange(8, 24, 4)
        fruits.append(Fruit(x_, y_, color_, width_, height_))


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
    for fruit in fruits:
        fruit.draw()
        if snake.elements[0][2].colliderect(fruit.hitbox):
            score += 1
            snake.add_size()
            fruits.remove(fruit)


FPS = 60
clock = pygame.time.Clock()
level_num = 1
score = 0
walls = []
fruits = []
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
        pygame.draw.rect(screen, (255, 255, 12), (0, i, 10, 10), 1)
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
    spawn_fruit()
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()
