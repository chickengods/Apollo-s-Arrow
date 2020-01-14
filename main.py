import pygame
import Apollo
import Arrow
import Enemy
WIN_WIDTH = 800
WIN_HEIGHT = 800

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

clock = pygame.time.Clock()

def draw_window(win, Apollo, arrow, Enemy):
    Apollo.draw(win)
    Enemy.draw(win)
    pygame.display.update()

def main_game(win, apollo, arrow):
    run = True
    while run:
        clock.tick(200)
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
        if arrow.mouse_position_queue_empty():
            arrow.move()
        apollo.move()
        draw_window(win, apollo, arrow, mob)
        mob.findApollo(apollo.x, apollo.y)


mob = Enemy.Enemy(0, 0)
test = Apollo.Apollo(400,400,5,100,100)
arrow = Arrow.Arrow(300,300,2)

main_game(win, test, arrow)

