import pygame
import math
pygame.init()
screen = pygame.display.set_mode((600, 600))

myPointsin = []
myPointcos = []
for x in range(0, 600):
    y = int(math.sin(x/600.0 * 6 * math.pi) * 200 + 300)
    myPointsin.append([x, y])
for x in range(0, 600):
    y = int(math.cos(x/600.0 * 6 * math.pi) * 200 + 300)
    myPointcos.append([x, y])

run = True
while run:
    pygame.time.delay(50)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.lines(screen, (255, 0, 0), False, myPointsin, 2)
    pygame.draw.lines(screen, (0, 0, 255), False, myPointcos, 2)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 600), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (600, 300), 1)

    pygame.display.update()

pygame.quit()
