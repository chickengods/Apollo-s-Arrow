import pygame
import Apollo
import os


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.img = pygame.image.load(os.path.join("imgs", "zombieImg.jpg"))
        self.hitbox = (self.x, self.y, 235, 235)

    def find_apollo(self, apolloX, apolloY):
        if apolloX > self.x:
            self.x += self.vel
        else:
            self.x -= self.vel
        if apolloY > self.y:
            self.y += self.vel
        else:
            self.y -= self.vel
        self.hitbox = (self.x, self.y, 235, 235)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        # uncomment if you want to see the hitbox
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
