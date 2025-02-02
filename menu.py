import pygame

import sys


pygame.init()

clock = pygame.time.Clock()


size = width, height = (1800, 990)
print(width, height)
scr = pygame.display.set_mode(size)
pygame.display.set_caption('Меню')
#scr.fill((230, 0, 0))
def menu(x_exit, y_exit, x_play, y_play, x_level, y_level):
    #size = width, height = (300, 200)
    next_wind = 'menu'
    f = pygame.image.load('pictures/Fon/Fon-1.jpg')
    window = pygame.display.set_mode(size)
    screen = pygame.Surface(size)

    font_exit = pygame.font.Font(None, 24)

    button_surface_exit = pygame.Surface((180, 70))

    text_exit = font_exit.render("Выход", True, (0, 0, 0))
    text_rect_exit = text_exit.get_rect(
        center=(button_surface_exit.get_width() / 2,
                button_surface_exit.get_height() / 2))

    button_rect_exit = pygame.Rect(x_exit, y_exit, 180, 70)
    ###
    font_play = pygame.font.Font(None, 64)

    button_surface_play = pygame.Surface((650, 140))

    text_play = font_play.render("Игра", True, (0, 0, 0))
    text_rect_play = text_play.get_rect(
        center=(button_surface_play.get_width() / 2,
                button_surface_play.get_height() / 2))

    button_rect_play = pygame.Rect(x_play, y_play, 650, 140)
    ###
    font_level = pygame.font.Font(None, 44)

    button_surface_level = pygame.Surface((550, 100))

    text_level = font_level.render("Уровень", True, (0, 0, 0))
    text_rect_level = text_level.get_rect(
        center=(button_surface_level.get_width() / 2,
                button_surface_level.get_height() / 2))

    button_rect_level = pygame.Rect(x_level, y_level, 550, 100)

    while True:
        clock.tick(60)
        window.blit(screen, (0, 0))
        screen.blit(f, (0, 0))


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if button_rect_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                ###
                if button_rect_play.collidepoint(event.pos):
                    print('hj')
                    next_wind = 'game'
                ###
                if button_rect_level.collidepoint(event.pos):
                    print('hj3')
                    next_wind = 'level'


        if button_rect_exit.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_exit, (189, 224, 255), (1, 1, 178, 68))
            pygame.draw.rect(button_surface_exit, (0, 0, 0), (0, 0, 179, 70), 2)
        else:
            pygame.draw.rect(button_surface_exit, (0, 0, 0), (0, 0, 180, 50))
            pygame.draw.rect(button_surface_exit, (186, 134, 112), (2, 2, 176, 68))
            pygame.draw.rect(button_surface_exit, (120, 85, 58), (-5, -10, 181, 78), 6)
            pygame.draw.rect(button_surface_exit, (0, 0, 0), (0, 0, 178, 70), 3)
            pygame.draw.rect(button_surface_exit, (0, 0, 0), (1, 1, 178, 70), 3)

        ###
        if button_rect_play.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_play, (189, 224, 255), (1, 1, 650, 140))
            pygame.draw.rect(button_surface_play, (0, 0, 0), (0, 0, 650, 140), 2)
        else:
            pygame.draw.rect(button_surface_play, (0, 0, 0), (1, 0, 449, 100))
            pygame.draw.rect(button_surface_play, (186, 134, 112), (1, 1, 650, 140))
            #pygame.draw.rect(button_surface_play, (255, 100, 0), (1, 0, 650, 140), 2)
            pygame.draw.rect(button_surface_play, (120, 85, 58), (-10, -10, 657, 147), 8)
            pygame.draw.rect(button_surface_play, (105, 60, 49), (-10, -10, 650, 140), 3)
            pygame.draw.rect(button_surface_play, (0, 0, 0), (0, 0, 650, 140), 4)
        ###
        if button_rect_level.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_level, (189, 224, 255), (1, 1, 550, 100))
        else:
            pygame.draw.rect(button_surface_level, (0, 0, 0), (0, 0, 550, 100))
            pygame.draw.rect(button_surface_level, (186, 134, 112), (1, 1, 550, 100))
            pygame.draw.rect(button_surface_level, (120, 85, 58), (-10, -10, 558, 108), 5)
            pygame.draw.rect(button_surface_level, (105, 60, 49), (-10, -10, 554, 104), 2)
            pygame.draw.rect(button_surface_level, (0, 0, 0), (0, 0, 550, 100), 3)

        # Показать текст кнопки
        button_surface_exit.blit(text_exit, text_rect_exit)
        button_surface_play.blit(text_play, text_rect_play)
        button_surface_level.blit(text_level, text_rect_level)
        # Нарисуйте кнопку на экране
        window.blit(button_surface_exit, (button_rect_exit.x, button_rect_exit.y))
        #scr.blit(screen, (1, 1))
        window.blit(button_surface_play, (button_rect_play.x, button_rect_play.y))
        #scr.blit(screen, (1, 1))
        window.blit(button_surface_level, (button_rect_level.x, button_rect_level.y))
        pygame.display.update()
        scr.blit(window, (1, 1))

    print(next_wind)




if __name__ == '__main__':
    #button_play(width//2, height//2)
    menu(width - 190, 20, width//2 - 350, height//2 - 100, width//2 - 280, height//2 + 150)

    #button_play(10, 10)
    #button(width//2 - 150, height//2 + 100, 250, 50, 'Game', 'play', scr)
    #button(width // 2 - 50, height // 2 + 10, 250, 50, 'Game', 'play', scr)
