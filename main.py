import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

clock = pygame.time.Clock()

def draw_window(win, Apollo):
    Apollo.draw(win)

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN():
            if event.key == pygame.K_w:
                # move
            if else event.key == pygame.K_a:
                # move
            if else event.key == pygame.K_s:

            if else event.key == pygame.K_d



        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()