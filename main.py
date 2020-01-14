import pygame
import Apollo

WIN_WIDTH = 800
WIN_HEIGHT = 800

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

clock = pygame.time.Clock()

def draw_window(win, Apollo):
    Apollo.draw(win)
    pygame.display.update()

def main_game(apollo, win):
    run = True
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    apollo.vel_change('w',1)
                if event.key == pygame.K_a:
                    apollo.vel_change('a',1)
                if event.key == pygame.K_s:
                    apollo.vel_change('s',1)
                if event.key == pygame.K_d:
                    apollo.vel_change('d',1)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    apollo.vel_change('w', -1)
                if event.key == pygame.K_s:
                    apollo.vel_change('s', -1)
                if event.key == pygame.K_a:
                    apollo.vel_change('a', -1)
                if event.key == pygame.K_d:
                    apollo.vel_change('d', -1)

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        apollo.move()
        draw_window(win, apollo)



test = Apollo.Apollo(400,400,5,100,100)

main_game(test, win)

