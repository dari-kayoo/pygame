import pygame
import random

pygame.init()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))
screen.fill((149, 218, 104))

witch = pygame.image.load(f'TSIS8/witch.png')
grasssize = 100

maxgrass = 30
myGrass = []
myGrass2 = []
i = 0
lining = pygame.image.load(f'TSIS8/line.png')
lining = pygame.transform.scale(lining, (100, 110))

fairies = []
for k in range(4):
    fairies.append(pygame.image.load(f'TSIS8/fairy{i}.png'))


pygame.display.set_caption("WITCH")


def showline(x, y):
    screen.blit(lining, (x, y))

class Grass():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.img = pygame.image.load(f'TSIS8/grass.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (grasssize, grasssize))

    def move(self):
        self.y += self.speed
        if self.y > height:
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


initialize_grass(maxgrass, myGrass, myGrass2)

run = True
while run:
    screen.fill((149, 218, 104))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    i += 5
    if i > 600:
        i = 0
    showline(355, i)
    pygame.draw.rect(screen, (113, 3, 161), (0, 0, 250, 600))
    pygame.draw.rect(screen, (113, 3, 161), (550, 0, 250, 600))
    screen.blit(witch, (360, 500))
    for g in myGrass:
        g.move()
        g.draw()
    for g1 in myGrass2:
        g1.move()
        g1.draw()
    pygame.display.update()
pygame.quit()
