import pygame
import random

pygame.init()
WITDH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WITDH, HEIGHT))
screen.fill((149, 218, 104))
# witch
witch_img = pygame.image.load(f'TSIS8/witch.png')
myWitch = []
# grass
grasssize = 100
maxgrass = 30
myGrass = []
myGrass2 = []
# line
i = 0
lining = pygame.image.load(f'TSIS8/line.png')
lining = pygame.transform.scale(lining, (100, 110))
# fairy
fairies_img = []
for k in range(4):
    fairies_img.append(pygame.image.load(f'TSIS8/fairy{i}.png'))

fairySize = 70
maxf = 20
myFairy = []

score = 0
pygame.display.set_caption("WITCH")
# line
def showline(x, y):
    screen.blit(lining, (x, y))
# witch
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
        self.hitbox = pygame.Rect(self.x, self.y, 100, 100)

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
        self.hitbox = pygame.Rect(self.x, self.y, 100, 100)
# fairy
class Fairy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.img = fairies_img[0]
        self.img = pygame.transform.scale(self.img, (fairySize, fairySize))
        # self.count = 0
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.maxf = maxf

    def draw_F(self):
        # self.count += 1
        # if self.count > 50:
        #     self.count = 0
        screen.blit(pygame.transform.scale(
            fairies_img[0], (fairySize, fairySize)), (self.x-20, self.y))
        self.hitbox = pygame.Rect(self.x, self.y, 100, 100)

    def fall(self):
        global score
        global maxf
        self.y += self.speed

        if self.hitbox.colliderect(myWitch[0].hitbox):
            myFairy.remove(self)
            score += 1
                
        if self.y > HEIGHT:
            self.y = 0 - fairySize    

def drawScore():
    global score
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f'Score:{score}', 1, (255, 255, 255))
    screen.blit(text, (20, 500))
  
# grass
class Grass():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.img = pygame.image.load(f'TSIS8/grass.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (grasssize, grasssize))

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0 - grasssize

# initializing
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
    y = 450
    myWitch.append(Witch(x, y))

def initialize_fairies(myFairy):
    for f in range(0, maxf):
        x = random.randint(250, 510)
        y = random.randint(0, 600)
        myFairy.append(Fairy(x, y))

initialize_grass(maxgrass, myGrass, myGrass2)
initialize_witch(myWitch)
initialize_fairies(myFairy)

run = True
FPS = 30
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
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
    #line
    i += 4
    if i > 600:
        i = 0
    showline(355, i)
    pygame.draw.rect(screen, (113, 3, 161), (0, 0, 250, 600))
    pygame.draw.rect(screen, (113, 3, 161), (550, 0, 250, 600))
    #grass
    for g in myGrass:
        g.move()
        g.draw()
    for g1 in myGrass2:
        g1.move()
        g1.draw()
    #witch
    for w in myWitch:
        w.draw_w()
        w.move_Witch()
    #fairy
    for f in myFairy:
        f.draw_F()
        f.fall()
    drawScore()
    pygame.display.update()
pygame.quit()
