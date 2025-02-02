import pygame

import sys


pygame.init()

clock = pygame.time.Clock()


size = width, height = (1800, 990)
print(width, height)
scr = pygame.display.set_mode(size)
pygame.display.set_caption('Меню')
f = pygame.image.load('pictures/Fon/Fon-6.png')
image = pygame.transform.scale(f, (size))
#scr.fill((230, 0, 0))
button_text = {1: 'Уровень 1', 2: 'Уровень 2', 3: 'Уровень 3',
               4: 'Уровень 4', 5: 'Уровень 5', 6: 'Уровень 6'}
def button(x, y, w, h, text): #action=None):
    font = pygame.font.Font(None, 60)
    text_but = font.render(text, True, (0, 0, 0))
    text_rect = text_but.get_rect(
        center=(x + (w // 2),
                y + (h // 2)))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(scr, (189, 224, 255), (x , y, w, h))
        scr.blit(text_but, text_rect)
        if click[0] == 1: #and action is not None:
            print(text)
            #action()

    else:
        pygame.draw.rect(scr, (186, 134, 112), (x, y, w, h))
        pygame.draw.rect(scr, (120, 85, 58), (x, y, w, h), 8)
        pygame.draw.rect(scr, (0, 0, 0), (x, y, w, h), 4)
        scr.blit(text_but, text_rect)



while True:
    clock.tick(60)
    scr.blit(image, (0, 0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        y = 200
        for i in range(1, 4):
            button(100, y, 750, 150, button_text[i])
            y += 200
        y = 200
        for j in range(4, 7):
            button(950, y, 750, 150, button_text[j])
            y += 200



        ###

        # Показать текст кнопки


        pygame.display.update()





if __name__ == '__main__':
    #button_play(width//2, height//2)
    level(100, 100, 650, 140, 6)

    #button_play(10, 10)
    #button(width//2 - 150, height//2 + 100, 250, 50, 'Game', 'play', scr)
    #button(width // 2 - 50, height // 2 + 10, 250, 50, 'Game', 'play', scr)
