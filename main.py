import pygame
import sys
from game import Board
#from game_over import game_over
#from win import win
from menu import menu
from levels import *
from dicts import button_text
from actions import *

pygame.init()
size = width, height = (1800, 990)
print(width, height)
scr = pygame.display.set_mode(size)
result = 'menu'
while True:
    if result == 'menu':
        result = menu(scr, width, height)
    elif result == 'game':
        result = game(scr)
    elif result == 'game_over':
        result = game_over(scr)
    elif result == 'level':
        result = level(scr, size)
    elif result == 'win':
        result = win(scr)
    else:
        break
