import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()