
import pygame
import math
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Zadanie 1")


# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)


radius = 150
cx=600/2
cy=600/2
deg = 0

def szesciokat(cx,cy,radius,deg):
    vertices =[]
    for i in range(6):
        angle = math.radians(60*i + deg)
        x= cx + radius * math.cos(angle)
        y= cy + radius * math.sin(angle)
        if transform4:
            k=0.2
            x = x+k*y
        if transform6:
            k=0.2
            y=y+k*x
        if transform7:
            (x,y) = (y,x)
        vertices.append((x,y))
    return vertices

transform4 = False
transform6=False
transform7 = False

run = True
while run:
    win.fill((0,0,0))
    punkty = szesciokat(cx,cy,radius,deg)
    hexagon= pygame.draw.polygon(win,ZOLTY,punkty,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                radius +=10
            if event.key == pygame.K_2:
                deg += 20
            if event.key == pygame.K_3:
                deg+=180
            if event.key == pygame.K_4:
                if not transform4:
                    transform4 = True
                else:
                    transform4 = False
            if event.key == pygame.K_5:
                cy-=10
            if event.key == pygame.K_6:
                if not transform6:
                    transform6 = True
                else:
                    transform6 = False
            if event.key == pygame.K_7:
                if not transform7:
                    transform7 = True
                else:
                    transform7 = False
                deg+=180
            if event.key == pygame.K_8:
                radius -=10
            if event.key == pygame.K_9:
                if not transform7:
                    transform7 = True
                else:
                    transform7 = False
                deg += 180
                if not transform4:
                    transform4 = True
                else:
                    transform4 = False
    pygame.display.update()