import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

size = width, height = (1800, 990)
print(width, height)
screen = pygame.display.set_mode(size)

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию


    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.left, self.top, self.cell_size, self.cell_size), 5  )
        print(self.cell_size)

if __name__ == '__main__':
    board = Board(5, 7)

    while True:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        board.set_view(0, 0, 150)
        board.render(screen)
        pygame.display.flip()

