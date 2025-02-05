import pygame

import sys

from actions import *
from dicts import button_text
pygame.init()
clock = pygame.time.Clock()

size = width, height = (1800, 990)
scr = pygame.display.set_mode(size)
def button(scr, x, y, w, h, text, text_size = 60, action = None): #action=None):
    font = pygame.font.Font(None, text_size)
    text_but = font.render(text, True, (0, 0, 0))
    text_rect = text_but.get_rect(
        center=(x + (w // 2),
                y + (h // 2)))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(scr, (189, 224, 255), (x , y, w, h))
        scr.blit(text_but, text_rect)
        if click[0] == 1 and action is not None:
            print(text)
            return 'menu'

    else:
        pygame.draw.rect(scr, (186, 134, 112), (x, y, w, h))
        pygame.draw.rect(scr, (120, 85, 58), (x, y, w, h), 8)
        pygame.draw.rect(scr, (0, 0, 0), (x, y, w, h), 4)
        scr.blit(text_but, text_rect)


def level(scr, size):
    pygame.display.set_caption('Меню')
    f = pygame.image.load('pictures/Fon/Fon-6.png')
    image = pygame.transform.scale(f, (size))
    while True:
        clock.tick(60)
        scr.blit(image, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            button(scr, 10, 10, 150, 50, 'Назад', 30, return_to_menu())
            y = 200
            for i in range(1, 4):
                button(scr, 100, y, 750, 150, button_text[i])
                y += 200
            y = 200
            for j in range(4, 7):
                button(scr, 950, y, 750, 150, button_text[j])
                y += 200

            pygame.display.update()

if __name__ == '__main__':
    level(scr, size)


