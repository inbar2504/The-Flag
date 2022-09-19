import pygame
import consts

def Solider(screen):
    solider_img = pygame.image.load('soldier.png')
    screen.blit(solider_img, [0, 0])
    pygame.display.flip()


