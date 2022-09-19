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

def print_bush(bush_matrix):
    for i in range(25):
        for j in range(50):
            if bush_matrix[i][j] == "bush":
                img.set_colorkey(consts.GREEN_BACKGROUND)
                screen.blit(img, [i*30, j*15])
    pygame.display.update()

def print_trap(full_matrix):
    for i in range(25):
        for j in range(50):
            if full_matrix[i][j] == "trap":
                img_trap.set_colorkey((20, 20, 20))
                screen.blit(img_trap, [i*30, j*15])
    pygame.display.update()

img = pygame.image.load(consts.IMAGE)
img_trap = pygame.image.load(consts.IMAGE_TRAP)
field_matrix = MineField.matrix_construction()
bush_matrix = MineField.fill_matrix(field_matrix, "bush")
full_matrix = MineField.fill_matrix(bush_matrix, "trap")
screen.fill(consts.GREEN_BACKGROUND)
print_bush(bush_matrix)

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
    print_bush(bush_matrix)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            finish = True
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
        print_trap(full_matrix)
        MineField.print_grid(screen, x, y)
        #print_bush(full_matrix)
pygame.quit()


