import random

import pygame
from Cell import Cell

pygame.init()
screen = pygame.display.set_mode((640, 640))
gameOver = False
group = pygame.sprite.Group()

possible_spaces = []
valid_coords = [160 * 0, 160 * 1, 160 * 2, 160 * 3]
for i in valid_coords:
    for x in valid_coords:
        possible_spaces.append([i, x])


def add_cell():
    spaces = possible_spaces.copy()
    if len(group) == 16:
        print("you lose")
        exit(0)
    for cell in group:
        try:
            spaces.remove([cell.rect.x, cell.rect.y])
        except ValueError:
            print(cell.rect.x, cell.rect.y)

    new_coords = random.choice(spaces)
    Cell(group, (255, 0, 0), new_coords[0], new_coords[1], 160, 160, random.choice([1, 2]))
    return


add_cell()
add_cell()

while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                tmp = [i for i in group]
                tmp.sort(key=lambda obj: obj.rect.x, reverse=True)
                for i in tmp:
                    i: Cell
                    i.move_right()
                add_cell()
            elif event.key == pygame.K_LEFT:
                tmp = [i for i in group]
                tmp.sort(key=lambda obj: obj.rect.x, reverse=False)
                for i in tmp:
                    i.move_left()
                add_cell()
            elif event.key == pygame.K_DOWN:
                tmp = [i for i in group]
                tmp.sort(key=lambda obj: obj.rect.y, reverse=True)
                print(len(tmp))
                for i in tmp:
                    i.move_down()
                add_cell()
            elif event.key == pygame.K_UP:
                tmp = [i for i in group]
                tmp.sort(key=lambda obj: obj.rect.y, reverse=False)
                for i in tmp:
                    i.move_up()
                add_cell()
        elif event.type == pygame.QUIT:
            exit(0)

    screen.fill((0, 0, 0))
    group.draw(screen)
    pygame.display.update()


