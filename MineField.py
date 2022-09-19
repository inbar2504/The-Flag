import pygame
import random
import consts
import Screen

def Flag(screen):
    flag_img = pygame.image.load('flag.png')
    screen.blit(flag_img, [900, 400])
    pygame.display.flip()

def matrix_construction():
    field_matrix = []
    for row in range(25):
        field_matrix.append([])
        for col in range(50):
            field_matrix[row].append("Free")
    return field_matrix

def fill_matrix(field_matrix, sigh, screen, img):
    count = 20
    for i in range(count):
        random_row = random.randint(1, 25)
        random_col = random.randint(1, 50)
        if field_matrix[random_row-1][random_col-1] == "Free":
            field_matrix[random_row-1][random_col-1] = sigh
            if sigh == "bush":
                img.set_colorkey(consts.GREEN_BACKGROUND)
                screen.blit(img, [random_row*30, random_col*15])
            pygame.display.flip()
        else:
            random_row = random.randint(1, 25)
            random_col = random.randint(1, 50)
            count += 1
    return (field_matrix)

def print_grid(screen):
    screen.fill((20, 20, 20))
    for x in range(0, 1000, 20):
        pygame.draw.line(screen, consts.COLOR_GRID, (1, x), (1000, x), 2)
        pygame.draw.line(screen, consts.COLOR_GRID, (x, 1), (x, 1000), 2)
        pygame.display.update()
    """
    screen.fill((0, 0, 0))
    pygame.display.flip()
   #create vrtical lines
    for i in range(1, 21):
        rect = pygame.Rect((i*consts.WINDOW_WIDTH, 0), (1, consts.WINDOW_HEIGHT))
        pygame.draw.rect(screen, consts.COLOR_GRID, rect)
    for i in range(1,21):
        rect = pygame.Rect((0, i*consts.WINDOW_WIDTH), (consts.WINDOW_HEIGHT, 1))
        pygame.draw.rect(screen, consts.COLOR_GRID, rect)
    """

field_matrix = []
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
img = pygame.image.load(consts.IMAGE).convert()
field_matrix = matrix_construction()
bush_matrix = fill_matrix(field_matrix, "bush", screen, img)
full_matrix = fill_matrix(bush_matrix, "trap", screen, img)
