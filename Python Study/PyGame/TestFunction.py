import pygame
from pygame.locals import *
import sys

sea_image = 'sea.jpg'
fish_image = 'fish.png'

pygame.init()

background = pygame.image.load(sea_image)
mouse_curson = pygame.image.load(fish_image)

width = background.get_width()
height = background.get_height()

screen = pygame.display.set_mode((width,height),FULLSCREEN,32)
pygame.display.set_caption('FIsh and sea')



while True:
    for event in pygame.event.get():
        if(event.type == QUIT):
            exit()
    screen.blit(background,(0,0))

    x,y = pygame.mouse.get_pos()

    x -= mouse_curson.get_width()/2
    y -= mouse_curson.get_height()/2

    screen.blit(mouse_curson,(x,y))

    pygame.display.update()
