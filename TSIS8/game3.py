import pygame
import random

pygame.init()
WITDH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WITDH, HEIGHT))
screen.fill((149, 218, 104))

witch_img = pygame.image.load(f'TSIS8/witch.png')

grasssize = 100

myWitch = []


maxgrass = 30
myGrass = []
myGrass2 = []
i = 0
lining = pygame.image.load(f'TSIS8/line.png')
lining = pygame.transform.scale(lining, (100, 110))


obstacles = []
fairies_img = []
for k in range(4):
    fairies_img.append(pygame.image.load(f'TSIS8/fairy{i}.png'))


pygame.display.set_caption("WITCH")


def showline(x, y):
    screen.blit(lining, (x, y))


class Witch():
    def __init__(self, x, y, speed=8):
        self.x = x
        self.y = y
        self.speed = speed
        self.up = True
        self.down = False
        self.left = False
        self.right = False
        self.img = witch_img

    def direction(self, right=False, left=False, down=False, up=False):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

    def move_Witch(self):
        if self.right:
            self.x += self.speed
        elif self.left:
            self.x -= self.speed
        # you handle where to sto0re screen width
        self.x = max(250, min(self.x, WITDH-350))
        self.y = max(0, min(self.y, HEIGHT))

    def draw_w(self):
        screen.blit(self.img, (self.x, self.y))


class Fairy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.img = fairies_img

    def draw_F(self):
        screen.blit(self.img, (self.x, self.y))

    def fall(self):
        self.y += self.speed


def spawner():
    if len(obstacles) < 3:
        # , (random.randint(
        obstacles.append(Fairy(random.randrange(220, 580, 20),
                         random.randrange(-500, -50, 100)))
        # 100, 130)#, random.randint(40, 60), random.randint(150, 170)), 16))


class Grass():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 1
        self.img = pygame.image.load(f'TSIS8/grass.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (grasssize, grasssize))

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0 - grasssize

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


def initialize_grass(maxgrass, myGrass, myGrass2):
    for i in range(0, maxgrass):
        x = random.randint(0, 200)
        y = random.randint(0, 600)
        myGrass.append(Grass(x, y))
    for i in range(0, maxgrass):
        x1 = random.randint(530, 800)
        y1 = random.randint(0, 600)
        myGrass2.append(Grass(x1, y1))


def initialize_witch(myWitch):
    x = 360
    y = 500
    myWitch.append(Witch(x, y))


initialize_grass(maxgrass, myGrass, myGrass2)
initialize_witch(myWitch)

run = True
while run:
    screen.fill((149, 218, 104))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # and myWitch[0].x < width - 400: #- myWitch[0].width:
    if keys[pygame.K_RIGHT] and myWitch[0].x < WITDH - 100:
        if myWitch[0].x > WITDH:
            myWitch[0].x = 0
        myWitch[0].direction(right=True)
        myWitch[0].move_Witch()

    elif keys[pygame.K_LEFT] and myWitch[0].x > 0:  # and myWitch[0].x > 360:
        if myWitch[0].x < 100:
            myWitch[0].x = 0
        myWitch[0].direction(left=True)
        myWitch[0].move_Witch()

    i += 5
    if i > 600:
        i = 0
    showline(355, i)
    pygame.draw.rect(screen, (113, 3, 161), (0, 0, 250, 600))
    pygame.draw.rect(screen, (113, 3, 161), (550, 0, 250, 600))

    for g in myGrass:
        g.move()
        g.draw()
    for g1 in myGrass2:
        g1.move()
        g1.draw()

    for w in myWitch:
        w.draw_w()
        w.move_Witch()
    spawner()

    pygame.display.update()
pygame.quit()
