import pygame
import os


class Apollo:



    def __init__(self, x, y, vel, health, armor):
        self.x = x
        self.y = y
        self.vel = vel
        self.health = health
        self.armor = armor
        self.img = pygame.image.load(os.path.join("imgs","linkImg.png"))

    def move(self, letter, vel):




    def draw(self, win):
        win.blit(self.img, (self.x,self.y))

