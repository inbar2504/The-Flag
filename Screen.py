import pygame
import random
import consts
import Soldier
pygame.init()
import MineField


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
solider_img = pygame.image.load('soldier.png')

finish = False
x = 0
y = 0

#InitScreen

while not finish:
    screen.fill(consts.GREEN_BACKGROUND)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= 1
    if keys[pygame.K_DOWN]:
        y += 1
    if keys[pygame.K_RIGHT]:
        x += 1
    if keys[pygame.K_LEFT]:
        x -= 1
    screen.blit(solider_img, (x, y))
    MineField.Flag(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            finish = True
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
        print("tal")
        MineField.print_grid(screen)
pygame.quit()

