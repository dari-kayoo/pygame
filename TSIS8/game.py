import pygame
pygame.init()
width = 400
height = 600
pygame.display.set_mode((400, 600))
background = pygame.Surface((400, 600))
background.fill((149, 218, 104))
road = pygame.Surface((200, height))
road.fill((203, 99, 219))

fairies = []
cars = []
for i in range(4):
    fairies.append(pygame.image.load(f"TSIS8/fairy{i}.png"))
for i in range(2):
    cars.append(pygame.image.load(f"TSIS8/mycar{i}.png"))


class Mycar(object):
    def __init__(self, x=10, y=10, speed=8):
        self.x = x
        self.y = y
        self.speed = speed
        self.up = True
        self.down = False
        self.left = False
        self.right = False

        def direction(self, right=False, left=False, down=False, up=False):
            self.right = right
            self.left = left
            self.up = up
            self.down = down

        def move(self):
            if self.right:
                self.x += self.speed
            elif self.left:
                self.x -= self.speed

        def fall(self):
            pass


class Car(Mycar):
    def __init__(self, x=10, y=10, speed=8, *cars):
        Mycar.__init__(self, x, y)
        self.cars = cars
        self.hitbox = pygame.cars


pygame.quit()
