import pygame
import Apollo
import Arrow
import Enemy


WIN_WIDTH = 1600
WIN_HEIGHT = 800

win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

clock = pygame.time.Clock()

def draw_window(win, apollo, arrow, enemies):
    win.fill((0,100,0))
    apollo.draw(win)
    for enemy in enemies:
        enemy.draw(win)
    arrow.draw(win)
    pygame.display.update()

def move_enemies (enemies, apollo):
    for enemy in enemies:
        enemy.find_apollo(apollo.x, apollo.y)
        apollo.check_hit(enemy)

def main_game(win, apollo, arrow, enemies):
    run = True
    while run:
        clock.tick(40)
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
        temp = pygame.mouse.get_pos()
        arrow.move2(temp[0], temp[1])
        apollo.move()
        move_enemies(enemies, apollo)
        draw_window(win, apollo, arrow, enemies)


mob = Enemy.Enemy(0, 0)
mob2 = Enemy.Enemy(700, 400)
test = Apollo.Apollo(400,400,2,100,100)
arrow = Arrow.Arrow(300,300,20)
enemies = (mob, mob2)
main_game(win, test, arrow, enemies)
#boi
