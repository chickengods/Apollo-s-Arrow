import pygame
import Apollo
import os


class Enemy:



    def __init__(self,x,y,):
        self.x = x
        self.y = y
        self.vel = 2
        self.img = pygame.image.load(os.path.join("imgs","zombieImg.jpg"))

    def findApollo(self, apolloX, apolloY):
        if apolloX > self.x:
            self.x += 1
        else:
            self.x -= 1
        if apolloY > self.y:
            self.y += 1
        else:
            self.y -= 1

    def draw(self, win):
        win.blit(self.img, (self.x,self.y))

