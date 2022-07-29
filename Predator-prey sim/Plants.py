import pygame as pg
from random import randint, uniform

pg.init()
plants = pg.sprite.Group()

PLANT_LEVEL = [(255, 255, 255),
               (124,252,0),
               (0,255,0),
               (34,139,34),
               (0,128,0),
               (0,100,0)]

class Plant(pg.sprite.Sprite):
    def __init__(self, x, y, ripeness, group):
        pg.sprite.Sprite.__init__(self)
        if ripeness != 0 and uniform(0, 1) < 0.7:
            self.image = pg.Surface((20, 20))
            self.ripeness = ripeness
            self.rect = self.image.get_rect(center = (x, y))
            self.image.fill(PLANT_LEVEL[self.ripeness - 1])
            self.add(group)

    def grow(self):
        if self.ripeness + 1 <= 5:
            self.ripeness += 1

    def minus_ripeness(self):
        if self.ripeness - 1 >= 0:
            self.ripeness -= 1

    def update(self):
        if self.ripeness == 0:
            self.image.fill(PLANT_LEVEL[self.ripeness])
        else:
            self.image.fill(PLANT_LEVEL[self.ripeness - 1])


def create_map(range_min, range_max, hight, width, group):
    centerx, centery = 10, 10
    for i in range(hight):
        for j in range(width):
            Plant(centerx, centery, randint(range_min, range_max+1), group)
            centerx += 20
        centery += 20
        centerx = 10

def update_map():
    for plant in plants:
        plant.grow()

