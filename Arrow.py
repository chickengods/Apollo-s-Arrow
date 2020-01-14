import pygame
import os

class Arrow:

    def __init__(self,x,y,vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.img = pygame.image.load(os.path.join("imgs", "arrow.png"))
        self.mouse_position_queue = []

    def add_to_mouse_queue(self,x,y):
        self.mouse_position_queue.append((x,y))

    def move(self):
        position = self.mouse_position_queue.pop(0)
        self.x = position[0]
        self.y = position[1]

    def mouse_position_queue_empty(self):
        return len(self.mouse_position_queue) != 0

    def draw(self, win):
        win.blit(self.img, (self.x,self.y))
