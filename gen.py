import numpy as np
import pygame as pg
from random import randint
from random import uniform

pg.init()

PLANT_LEVEL = [(255, 255, 255),
               (124,252,0),
               (0,255,0),
               (34,139,34),
               (0,128,0),
               (0,100,0)]

class Plant(pg.sprite.Sprite):
    def __init__(self, x, y, ripeness, group):  #surf
        pg.sprite.Sprite.__init__(self)
        if ripeness != 0 and uniform(0, 1) < 0.15: #only 15 percents of map are not empty
            self.image = pg.Surface((20, 20))
            self.ripeness = ripeness
            self.rect = self.image.get_rect(center = (x, y))
            self.image.fill(PLANT_LEVEL[self.ripeness - 1])
            self.add(group)
    def grow(self):
        pass


def create_map(range_min, range_max, hight, width, group):
    centerx, centery = 10, 10
    for i in range(hight):
        for j in range(width):
            Plant(centerx, centery, randint(range_min, range_max + 1), group)
            centerx += 20
        centery += 20
        centerx = 10

plants = pg.sprite.Group()
create_map(0, 5, 50, 50, plants)

def gen_wolf(amount,x,y):
    if(amount == 1):
        new_wolf = animals.Wolf(random.randint(50, 100), random.randint(10, 50), random.randint(1, 3))
        return new_wolf
    elif(amount > 1):
        Wolves = []
        for i in range(amount):
          new_wolf = animals.Wolf(random.randint(50, 100), random.randint(10, 50), random.randint(1, 3))
          Wolves.append(new_wolf)
        return Wolves
def gen_fox(amount,x,y):
    if(amount == 1):
        new_fox = animals.Fox(random.randint(40, 80), random.randint(10, 50), random.randint(1, 2))
        return new_fox
    elif(amount > 1):
        Foxes = []  #generate_wolf(amount,x,y)
        for i in range(amount):
          new_fox = animals.Fox(random.randint(40, 80), random.randint(10, 50), random.randint(1, 2))
          Foxes.append(new_fox)
        return Foxes
def gen_rabbit(amount,x,y):
    if(amount == 1):
        new_rabbit = animals.Rabbit(random.randint(20, 40), random.randint(10, 50), random.randint(1, 2))
        return new_rabbit
    elif(amount > 1):
        Rabbits = []
        for i in range(amount):
          new_rabbit = animals.Rabbit(random.randint(20, 40), random.randint(10, 50), random.randint(1, 2))
          Rabbit.append(new_rabbit)
        return Rabbit
def gen_bird(amount,x,y):
    if(amount == 1):
        new_bird = animals.Bird(random.randint(15, 30), random.randint(10, 50), random.randint(1, 2))
        return new_bird
    elif(amount > 1):
        Birds = []
        for i in range(amount):
          new_bird = animals.Bird(random.randint(15, 30), random.randint(10, 50), random.randint(1, 2))
          Birds.append(new_bird)
        return Birds
