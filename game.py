import sys, pygame
import m
import networkx as nx

ma = m.M(20)
pygame.init()

size = width, height = 800, 600
bordersize = 100
speed = [1, 1]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

for coord in nx.drawing.spring_layout(ma.m).values():
    xy = (int(((coord[0]*(width-bordersize))/2)+(width/2)),int(((coord[1]*(height-bordersize))/2)+(height/2)))
    pygame.draw.circle(screen,(255,0,0),xy,15)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    
