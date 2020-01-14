import pygame
import os


class Apollo:

    faceUp = "apolloUp.png"
    faceDown = "apolloDown.png"
    faceLeft = "apolloLeft.png"
    faceRight = "apolloRight.png"

    def __init__(self,x,y,vel,health,armor):
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.vel = vel
        self.health = health
        self.armor = armor
        self.currImg = pygame.image.load(os.path.join("imgs","apolloLeft.png"))

    def vel_change(self, letter, num):
        if letter == 'w':
            self.currImg = pygame.image.load(os.path.join("imgs","apolloUp.png"))
            self.y_vel = self.y_vel - self.vel * num
        elif letter == 's':
            self.currImg = pygame.image.load(os.path.join("imgs", "apolloDown.png"))
            self.y_vel = self.y_vel + self.vel * num
        elif letter == 'a':
            self.currImg = pygame.image.load(os.path.join("imgs", "apolloLeft.png"))
            self.x_vel = self.x_vel - self.vel * num
        elif letter == 'd':
            self.currImg = pygame.image.load(os.path.join("imgs","apolloRight.png"))
            self.x_vel = self.x_vel + self.vel * num

    def vel_zero(self, num):
        if num == 1:
            self.y_vel = 0
        else:
            self.x_vel = 0


    def move(self):
        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel




    def draw(self, win):
        win.blit(self.currImg, (self.x,self.y))

