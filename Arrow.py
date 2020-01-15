import pygame
import os
import numpy as np
import math

class Arrow:

    def __init__(self,x,y,vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.delay = 0
        self.img = pygame.image.load(os.path.join("imgs", "arrow.png"))
        self.mouse_position_queue = []

    def add_to_mouse_queue(self,x,y):
        if len(self.mouse_position_queue) == 0:
            self.mouse_position_queue.append((x,y))
        else:
            x1 = self.mouse_position_queue[-1][0]
            y1 = self.mouse_position_queue[-1][1]
            for point in self.find_all_points_between_two_points(x1,y1,x,y):
                x = point[0]
                y = point[1]
                self.mouse_position_queue.append((x,y))


    def find_all_points_between_two_points(self, x1, y1, x2, y2):
        d = np.array([[x1, y1], [x2, y2]])
        rise = d[0, 1] - d[1, 1]
        run = d[0, 0] - d[1, 0]
        slope = rise / run


        sign = 1
        if (slope < 0):
            sign = -1
        points = ([round(d[0, 0] + sign * i), round(math.floor(d[0, 1] + (sign * i * slope)))] for i in
                  range(1 + int(math.ceil(abs(d[0, 0] - d[1, 0])))))
        return points

    def move(self):
        if self.delay == self.vel:
            position = self.mouse_position_queue.pop(0)
            self.x = position[0]
            self.y = position[1]
            self.delay = self.delay - self.vel
        else:
            self.delay = self.delay + 1

    def move_towards_mouse(self, x, y):
        distance = [(x - self.x), (y - self.y)]

        norm = math.sqrt(distance[0] ** 2 + distance[1]**2)
        if norm != 0:
            direction = [(distance[0]/norm), (distance[1]/norm)]
            self.x = x + direction[0] * self.vel
            self.y = y + direction[1] * self.vel

    def move2(self,x,y):
        if x > self.x:
            self.x += self.vel
        else:
            self.x -= self.vel
        if y > self.y:
            self.y += self.vel
        else:
            self.y -= self.vel








    def mouse_position_queue_empty(self):
        return len(self.mouse_position_queue) != 0

    def draw(self, win):
        win.blit(self.img, (self.x,self.y))
        #if len(self.mouse_position_queue) > 2:
         #   pygame.draw.lines(win, (100,0,0), False, self.mouse_position_queue)

