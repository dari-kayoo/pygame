import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((149, 218, 104))
witch = pygame.image.load(f'TSIS8/witch.png')

i = 0
lining = pygame.image.load(f'TSIS8/line.png')
lining = pygame.transform.scale(lining, (100, 110))

def showline(x, y):
    screen.blit(lining, (x, y))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((149, 218, 104))
    i += 5
    if i > 600:
        i = 0
    showline(375, i)

    screen.blit(witch, (375, 500))
    pygame.display.update()
pygame.quit()
