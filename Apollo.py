import pygame
import os


class Apollo:
    WIN_WIDTH = 1600
    WIN_HEIGHT = 800
    faceUp = "apolloUp.png"
    faceDown = "apolloDown.png"
    faceLeft = "apolloLeft.png"
    faceRight = "apolloRight.png"
    gold = 0;

    def __init__(self,x,y,vel,health,armor):
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.vel = vel
        self.health = health
        self.armor = armor
        self.currImg = pygame.image.load(os.path.join("imgs","apolloLeft.png"))
        self.hitbox = (self.x, self.y, 32, 52)

    def vel_change(self, letter, num):
        if letter == 'w':
            if (num > 0):
                self.currImg = pygame.image.load(os.path.join("imgs","apolloUp.png"))
            self.y_vel = self.y_vel - self.vel * num
        elif letter == 's':
            if (num > 0):
                self.currImg = pygame.image.load(os.path.join("imgs", "apolloDown.png"))
            self.y_vel = self.y_vel + self.vel * num
        elif letter == 'a':
            if (num > 0):
                self.currImg = pygame.image.load(os.path.join("imgs", "apolloLeft.png"))
            self.x_vel = self.x_vel - self.vel * num
        elif letter == 'd':
            if (num > 0):
                self.currImg = pygame.image.load(os.path.join("imgs","apolloRight.png"))
            self.x_vel = self.x_vel + self.vel * num

    def vel_zero(self, num):
        if num == 1:
            self.y_vel = 0
        else:
            self.x_vel = 0


    def give_gold (self, num):
        gold += num


    def move(self):
        newX = self.x + self.x_vel
        newY = self.y + self.y_vel
        # new X and new Y are used to determine whether Apollo will be outside of the screen
        # if he were to move with the given velocity, if so, it will not move him
        if 0 < newX < (self.WIN_WIDTH - 30):
            self.x = newX
        if 0 < newY < (self.WIN_HEIGHT - 40):
            self.y = newY
        self.hitbox = (self.x, self.y, 32, 52)

    def check_hit (self, enemy):
        # check if apollo within x bounds of enemy hitbox
        if (enemy.x < self.x < (enemy.x + enemy.hitbox[2]) or enemy.x < (self.x + self.hitbox[2]) < (enemy.x + enemy.hitbox[2])):
            # it is within bounds of the x axis
            # check if within bounsd of y hitbox
            if (enemy.y < self.y < (enemy.y + enemy.hitbox[3]) or enemy.y < (self.y + self.hitbox[3]) < (enemy.y + enemy.hitbox[3])):
                self.x = 1000
                self.y = 1000



    def draw(self, win):
        win.blit(self.currImg, (self.x,self.y))
        # uncomment if you want to see hitbox
        pygame.draw.rect(win, (255, 0,0), self.hitbox, 2)

