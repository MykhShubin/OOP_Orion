import sys

import pygame as pg
from Button import Button
from math import *
from Animals import *
from Plants import *


pg.init()
TIMER = pg.USEREVENT+1

W, H = 1300, 1000
sc = pg.display.set_mode((W, H), pg.RESIZABLE)
pg.time.set_timer(pg.USEREVENT, 200)
pg.time.set_timer(TIMER, 1500)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128,128,128)
YELLOW = (255,255,0)

clock = pg.time.Clock()
FPS = 20
time_elapsed_since_last_action = 0

angle_pred = 0
angle_prey = 0
angle_plant = 0
max_satiety = 500
nutriens = 90
prey_breed_time = 150
pred_breed_time = max_satiety/1.5 - nutriens

foxes = pg.sprite.Group()
bears = pg.sprite.Group()
rabbits = pg.sprite.Group()
birds = pg.sprite.Group()

###################################################


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pg.font.Font("font.ttf", size)

def update_text(rabbit_c,fox_c,bear_c,bird_c):
    predators_c = get_font(15).render('Predators', True, WHITE)
    predator_text = predators_c.get_rect(topleft=(W - 250, 300))
    sc.blit(predators_c, predator_text)

    prey_c = get_font(20).render('Prey', True, WHITE)
    prey_text = prey_c.get_rect(topleft=(W - 250, 150))
    sc.blit(prey_c, prey_text)

    fox_pred = get_font(20).render(' Fox = ', True, ORANGE)
    fox_text = fox_pred.get_rect(topleft=(W - 250, 350))
    sc.blit(fox_pred, fox_text)

    fox_pred = get_font(15).render(str(fox_c), True, ORANGE)
    fox_text = fox_pred.get_rect(topleft=(W - 130, 350))
    sc.blit(fox_pred, fox_text)

    bear_pred = get_font(15).render(' Bear = ', True, YELLOW)
    bear_text = bear_pred.get_rect(topleft=(W - 250, 380))
    sc.blit(bear_pred, bear_text)

    bear_pred = get_font(15).render(str(bear_c), True, YELLOW)
    bear_text = bear_pred.get_rect(topleft=(W - 130, 380))
    sc.blit(bear_pred, bear_text)

    rabbit_prey = get_font(15).render(' Rabbit = ', True, GRAY)
    rabbit_text = rabbit_prey.get_rect(topleft=(W - 250, 190))
    sc.blit(rabbit_prey, rabbit_text)

    rabbit_prey = get_font(15).render(str(rabbit_c), True, GRAY)
    rabbit_text = rabbit_prey.get_rect(topleft=(W - 100, 190))
    sc.blit(rabbit_prey, rabbit_text)

    bird_prey = get_font(15).render(' Bird = ', True, BLUE)
    bird_text = bird_prey.get_rect(topleft=(W - 250, 220))
    sc.blit(bird_prey, bird_text)

    bird_prey = get_font(15).render(str(bird_c), True, BLUE)
    bird_text = bird_prey.get_rect(topleft=(W - 100, 220))
    sc.blit(bird_prey, bird_text)

def Draw(group):
    for animal in group:
        sc.blit(animal.vision_surf, animal.vision)
        sc.blit(animal.image, animal.rect)

def create_animal(group,x,y):
    if x == None or y == None:
        x = randint(50, W - 325)
        y = randint(50, H - 50)
    speed_pred = randint(4, 5)
    speed_prey = randint(2, 3)
    phi = randint(0, 360)
    satiety_prey = randint(5, 7)
    satiety_pred = randint(max_satiety/2-nutriens, max_satiety/2)

    if group == foxes:
        color = ORANGE
        Fox(x, y, phi, speed_pred,satiety_pred, color, group)
    elif group == bears:
        color = YELLOW
        Bear(x, y, phi, speed_pred, satiety_pred, color, group)
    elif group == rabbits:
        color = GRAY
        Rabbit(x, y, phi, speed_prey, satiety_prey, color, group)
    elif group == birds:
        color = BLUE
        Bird(x, y, phi, speed_prey, satiety_prey, color, group)

def calc_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)
    return degs

def eat_prey(prey, predator):
    if predator.rect.colliderect(prey.rect):
        prey.kill()
        if predator.satiety <= (max_satiety - nutriens):
            predator.satiety += nutriens

def eat_grass(prey, plant):
    if plant.rect.colliderect(prey.rect):
        plant.minus_ripeness()
        prey.satiety = prey.satiety+nutriens/4

def breed(anim1, anim2):
    if anim1.group == rabbits and anim2.group == rabbits:
        create_animal(rabbits, anim1.rect.centerx, anim1.rect.centery)
        anim1.satiety = anim1.satiety / 4
        anim2.satiety = anim2.satiety / 4
    if anim1.group == foxes and anim2.group == foxes:
        create_animal(foxes, anim1.rect.centerx, anim1.rect.centery)
        anim1.satiety = anim1.satiety/3
        anim2.satiety = anim2.satiety/3
    if anim1.group == birds and anim2.group == birds:
        create_animal(birds, anim1.rect.centerx, anim1.rect.centery)
        anim1.satiety = anim1.satiety / 4
        anim2.satiety = anim2.satiety / 4
    if anim1.group == bears and anim2.group == bears:
        create_animal(bears, anim1.rect.centerx, anim1.rect.centery)
        anim1.satiety = anim1.satiety/3
        anim2.satiety = anim2.satiety/3

def death():
    for fox in foxes:
        if fox.satiety <= 0:
            fox.kill()
    for bear in bears:
        if bear.satiety <=0:
            bear.kill()

def collide():
    for fox in foxes:#foxes eat prey and breed
        if fox.satiety <= pred_breed_time:
            for rabbit in rabbits:
                if fox.vision.colliderect(rabbit.rect):
                    if fox.satiety <= max_satiety/2:
                        angle_pred = calc_angle(fox.rect.centerx, fox.rect.centery, rabbit.rect.centerx, rabbit.rect.centery)
                        fox.update(H, W-305, angle_pred)
                        eat_prey(rabbit, fox)
            for bird in birds:
                if fox.vision.colliderect(bird.rect):
                    if fox.satiety <= max_satiety/2:
                        angle_pred = calc_angle(fox.rect.centerx, fox.rect.centery, bird.rect.centerx, bird.rect.centery)
                        fox.update(H, W-305, angle_pred)
                        eat_prey(bird, fox)
        else:
            for fox2 in foxes:
                if fox != fox2:
                    if fox.vision.colliderect(fox2.rect):
                        if fox2.satiety > pred_breed_time:
                            angle_pred = calc_angle(fox.rect.centerx, fox.rect.centery, fox2.rect.centerx, fox2.rect.centery)
                            fox.update(H, W-305, angle_pred)
                            breed(fox, fox2)

    for bear in bears:#bears eat prey and breed
        if bear.satiety <= pred_breed_time:
            for rabbit in rabbits:
                if bear.vision.colliderect(rabbit.rect):
                    if bear.satiety <= max_satiety/2:
                        angle_pred = calc_angle(bear.rect.centerx, bear.rect.centery, rabbit.rect.centerx, rabbit.rect.centery)
                        bear.update(H, W-305, angle_pred)
                        eat_prey(rabbit, bear)
            for bird in birds:
                if bear.vision.colliderect(bird.rect):
                    if bear.satiety <= max_satiety/2:
                        angle_pred = calc_angle(bear.rect.centerx, bear.rect.centery, bird.rect.centerx, bird.rect.centery)
                        bear.update(H, W-305, angle_pred)
                        eat_prey(bird, bear)
        else:
            for bear2 in bears:
                if bear != bear2:
                    if bear.vision.colliderect(bear2.rect):
                        if bear2.satiety > pred_breed_time:
                            angle_pred = calc_angle(bear.rect.centerx, bear.rect.centery, bear2.rect.centerx, bear2.rect.centery)
                            bear.update(H, W-305, angle_pred)
                            breed(bear, bear2)

    for rabbit in rabbits:#rabbits breed and eat
        if rabbit.satiety >= prey_breed_time:
            for rabbit2 in rabbits:
                if rabbit != rabbit2:
                    if rabbit.vision.colliderect(rabbit2.rect):
                        if rabbit.satiety >= prey_breed_time and rabbit2.satiety >= prey_breed_time:
                            angle_prey = calc_angle(rabbit.rect.centerx, rabbit.rect.centery, rabbit2.rect.centerx, rabbit2.rect.centery)
                            rabbit.update(H, W-305, angle_prey)
                            if rabbit.rect.colliderect(rabbit2.rect):
                                breed(rabbit, rabbit2)
        else:
            for plant in plants:
                if rabbit.vision.colliderect(plant.rect) and plant.ripeness >= 1:
                    angle_plant = calc_angle(rabbit.rect.centerx, rabbit.rect.centery, plant.rect.centerx, plant.rect.centery)
                    rabbit.update(H, W-305, angle_plant)
                    eat_grass(rabbit,plant)

    for bird in birds:#birds breed and eat
        if bird.satiety >= prey_breed_time:
            for bird2 in birds:
                if bird != bird2:
                    if bird.vision.colliderect(bird2.rect):
                        if bird.satiety >= prey_breed_time and bird2.satiety >= prey_breed_time:
                            angle_prey = calc_angle(bird.rect.centerx, bird.rect.centery, bird2.rect.centerx, bird2.rect.centery)
                            bird.update(H, W-305, angle_prey)
                            if bird.rect.colliderect(bird2.rect):
                                breed(bird, bird2)
        else:
            for plant in plants:
                if bird.vision.colliderect(plant.rect) and plant.ripeness >= 1:
                    angle_plant = calc_angle(bird.rect.centerx, bird.rect.centery, plant.rect.centerx, plant.rect.centery)
                    bird.update(H, W, angle_plant)
                    eat_grass(bird,plant)
