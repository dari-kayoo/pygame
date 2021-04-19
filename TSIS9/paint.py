import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

pygame.display.set_caption('Paint')


def drawLine(screen, start, end, color, radius):
    # coordinates
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]
    x_ = abs(x1 - x2)
    y_ = abs(y1 - y2)
    if x_ > y_:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (- (x2 * y1 - x1 * y2) - (y2 - y1) * x) / (x1 - x2)
            pygame.draw.circle(screen, color, (x, y), radius)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-(x2 * y1 - x1 * y2) - (x1 - x2) * y) / (y2 - y1)
            pygame.draw.circle(screen, color, (x, y), radius)


def paint():
    mode = 'black'
    drawing = False
    lastPos = (0, 0)
    color = (255, 128, 0)
    radius = 2
    width, height = 5, 6
    colors = {
        'eraser': (255, 255, 255),
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'black': (0, 0, 0)
    }
    run = True
    while run:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'black':
                    color = ((0, 0, 0))
                else:
                    color = colors[mode]
                pygame.draw.circle(screen, color, event.pos, radius)
                drawing = True


            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    drawLine(screen, lastPos, event.pos, color, radius)
                lastPos = event.pos

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    mode = 'eraser'
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_l:
                    mode = 'black'

                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
            

        pygame.display.update()
    pygame.quit()


paint()
