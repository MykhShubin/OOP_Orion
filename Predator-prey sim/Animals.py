import pygame as pg
import math

def to_radians(degrees):
    return degrees * (math.pi / 180)

def to_degrees(radians):
    return (180 * radians) / math.pi

transp = 0

class Fox(pg.sprite.Sprite):
    def __init__(self, x, y, phi, speed, satiety, color, group):  #surf
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15)) #20, 20
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))

        self.speed = speed
        self.phi = to_radians(phi)
        self.satiety = satiety
        self.group = group

        self.vision_surf = pg.Surface((self.image.get_width() + 50, self.image.get_height() + 50), pg.SRCALPHA)
        self.vision = self.vision_surf.get_rect(center = self.rect.center)
        #s_vision = pg.Rect((s_rect.center), (s.get_width() + 100, s.get_height() + 100))
        self.vision_surf.fill((200, 100, 0, transp))

##        self.s_vision_surf =
##        self.s_vision = pg.Rect((self.rect.center), (self.image.get_width() + 50, self.image.get_height() + 50))

        self.add(group)

    def update(self, *args):
        if self.satiety > 0:
            self.satiety -= 2
        if args[2] != None:
            self.phi = to_radians(args[2])
            return
        if self.rect.top <= 0:
            if self.phi > to_radians(90):
                self.phi += (2 * (to_radians(180) - self.phi))
            elif self.phi == to_radians(90):
                self.phi = to_radians(270)
            elif self.phi < to_radians(90):
                self.phi = (to_radians(360) - self.phi)

        if self.rect.right >= args[1]:
            if self.phi > to_radians(0):
                self.phi = (to_radians(180) - self.phi)
            elif self.phi == to_radians(0):
                self.phi = to_radians(180)
            elif self.phi < to_radians(0):
                #self.phi = (to_radians(540) - self.phi) #540
                self.phi = to_radians(200)

        if self.rect.bottom >= args[0]:
            if self.phi > to_radians(270):
                self.phi = (to_radians(360) - self.phi)
            elif self.phi == to_radians(270):
                self.phi = to_radians(90)
            elif self.phi < to_radians(270):
                self.phi = (to_radians(360) - self.phi) ########

        if self.rect.left <= 0:
            if self.phi > to_radians(180):
                self.phi = (to_radians(540) - self.phi)
            elif self.phi == to_radians(180):
                self.phi = to_radians(0)
            elif self.phi < to_radians(180):
                self.phi = (to_radians(180) - self.phi)


        delta_x = int(self.speed * (math.cos(self.phi)))
        delta_y = int(self.speed * (math.sin(self.phi)))

        if 0 <= self.phi < 90:
            self.rect.x += delta_x #+
            self.rect.y -= delta_y #-
        elif 90 <= self.phi < 180:
            self.rect.x -= delta_x #-
            self.rect.y -= delta_y #-
        elif 180 <= self.phi < 270:
            self.rect.x -= delta_x #-
            self.rect.y += delta_y #+
        elif 270 <= self.phi < 360:
            self.rect.x += delta_x #+
            self.rect.y += delta_y #+

        self.vision.center = self.rect.center


class Bear(pg.sprite.Sprite):
    def __init__(self, x, y, phi, speed, satiety, color, group):  #surf
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15)) #20, 20
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))

        self.speed = speed
        self.phi = to_radians(phi)
        self.satiety = satiety
        self.group = group

        self.vision_surf = pg.Surface((self.image.get_width() + 50, self.image.get_height() + 50), pg.SRCALPHA)
        self.vision = self.vision_surf.get_rect(center = self.rect.center)
        self.vision_surf.fill((255, 255, 0, transp))

        self.add(group)

    def update(self, *args):
        if self.satiety > 0:
            self.satiety -= 2
        if args[2] != None:
            self.phi = to_radians(args[2])
            return
        if self.rect.top <= 0:
            if self.phi > to_radians(90):
                self.phi += (2 * (to_radians(180) - self.phi))
            elif self.phi == to_radians(90):
                self.phi = to_radians(270)
            elif self.phi < to_radians(90):
                self.phi = (to_radians(360) - self.phi)

        if self.rect.right >= args[1]:
            if self.phi > to_radians(0):
                self.phi = (to_radians(180) - self.phi)
            elif self.phi == to_radians(0):
                self.phi = to_radians(180)
            elif self.phi < to_radians(0):
                self.phi = to_radians(200)

        if self.rect.bottom >= args[0]:
            if self.phi > to_radians(270):
                self.phi = (to_radians(360) - self.phi)
            elif self.phi == to_radians(270):
                self.phi = to_radians(90)
            elif self.phi < to_radians(270):
                self.phi = (to_radians(360) - self.phi)

        if self.rect.left <= 0:
            if self.phi > to_radians(180):
                self.phi = (to_radians(540) - self.phi)
            elif self.phi == to_radians(180):
                self.phi = to_radians(0)
            elif self.phi < to_radians(180):
                self.phi = (to_radians(180) - self.phi)


        delta_x = int(self.speed * (math.cos(self.phi)))
        delta_y = int(self.speed * (math.sin(self.phi)))

        if 0 <= self.phi < 90:
            self.rect.x += delta_x #+
            self.rect.y -= delta_y #-
        elif 90 <= self.phi < 180:
            self.rect.x -= delta_x #-
            self.rect.y -= delta_y #-
        elif 180 <= self.phi < 270:
            self.rect.x -= delta_x #-
            self.rect.y += delta_y #+
        elif 270 <= self.phi < 360:
            self.rect.x += delta_x #+
            self.rect.y += delta_y #+

        self.vision.center = self.rect.center


class Rabbit(pg.sprite.Sprite):
    def __init__(self, x, y, phi, speed, satiety, color, group):  #surf
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = speed
        self.phi = to_radians(phi)
        self.satiety = satiety
        self.group = group

        self.vision_surf = pg.Surface((self.image.get_width() + 50, self.image.get_height() + 50), pg.SRCALPHA)
        self.vision = self.vision_surf.get_rect(center = self.rect.center)
        self.vision_surf.fill((128, 128, 128, transp))

        self.add(group)

    def update(self, *args):
        if self.satiety > 0:
            self.satiety -= 1
        if args[2] != None:
            self.phi = to_radians(args[2])
            return
        if self.rect.top <= 0:
            if self.phi > to_radians(90):
                self.phi += (2 * (to_radians(180) - self.phi))
            elif self.phi == to_radians(90):
                self.phi = to_radians(270)
            elif self.phi < to_radians(90):
                self.phi = (to_radians(360) - self.phi)

        if self.rect.right >= args[1]:
            if self.phi > to_radians(0):
                self.phi = (to_radians(180) - self.phi)
            elif self.phi == to_radians(0):
                self.phi = to_radians(180)
            elif self.phi < to_radians(0):
                #self.phi = (to_radians(540) - self.phi) #540
                self.phi = to_radians(200)

        if self.rect.bottom >= args[0]:
            if self.phi > to_radians(270):
                self.phi = (to_radians(360) - self.phi)
            elif self.phi == to_radians(270):
                self.phi = to_radians(90)
            elif self.phi < to_radians(270):
                self.phi = (to_radians(360) - self.phi) ########

        if self.rect.left <= 0:
            if self.phi > to_radians(180):
                self.phi = (to_radians(540) - self.phi)
            elif self.phi == to_radians(180):
                self.phi = to_radians(0)
            elif self.phi < to_radians(180):
                self.phi = (to_radians(180) - self.phi)


        delta_x = int(self.speed * (math.cos(self.phi)))
        delta_y = int(self.speed * (math.sin(self.phi)))

        if 0 <= self.phi < 90:
            self.rect.x += delta_x #+
            self.rect.y -= delta_y #-
        elif 90 <= self.phi < 180:
            self.rect.x -= delta_x #-
            self.rect.y -= delta_y #-
        elif 180 <= self.phi < 270:
            self.rect.x -= delta_x #-
            self.rect.y += delta_y #+
        elif 270 <= self.phi < 360:
            self.rect.x += delta_x #+
            self.rect.y += delta_y #+

        self.vision.center = self.rect.center


class Bird(pg.sprite.Sprite):
    def __init__(self, x, y, phi, speed, satiety, color, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = speed
        self.phi = to_radians(phi)
        self.satiety = satiety
        self.group = group

        self.vision_surf = pg.Surface((self.image.get_width() + 50, self.image.get_height() + 50), pg.SRCALPHA)
        self.vision = self.vision_surf.get_rect(center = self.rect.center)
        self.vision_surf.fill((0,0,255, transp))

        self.add(group)


    def update(self, *args):
        if self.satiety > 0:
            self.satiety -= 1
        if args[2] != None:
            self.phi = to_radians(args[2])
            return
        if self.rect.top <= 0:
            if self.phi > to_radians(90):
                self.phi += (2 * (to_radians(180) - self.phi))
            elif self.phi == to_radians(90):
                self.phi = to_radians(270)
            elif self.phi < to_radians(90):
                self.phi = (to_radians(360) - self.phi)

        if self.rect.right >= args[1]:
            if self.phi > to_radians(0):
                self.phi = (to_radians(180) - self.phi)
            elif self.phi == to_radians(0):
                self.phi = to_radians(180)
            elif self.phi < to_radians(0):
                self.phi = to_radians(200)

        if self.rect.bottom >= args[0]:
            if self.phi > to_radians(270):
                self.phi = (to_radians(360) - self.phi)
            elif self.phi == to_radians(270):
                self.phi = to_radians(90)
            elif self.phi < to_radians(270):
                self.phi = (to_radians(360) - self.phi)

        if self.rect.left <= 0:
            if self.phi > to_radians(180):
                self.phi = (to_radians(540) - self.phi)
            elif self.phi == to_radians(180):
                self.phi = to_radians(0)
            elif self.phi < to_radians(180):
                self.phi = (to_radians(180) - self.phi)


        delta_x = int(self.speed * (math.cos(self.phi)))
        delta_y = int(self.speed * (math.sin(self.phi)))

        if 0 <= self.phi < 90:
            self.rect.x += delta_x #+
            self.rect.y -= delta_y #-
        elif 90 <= self.phi < 180:
            self.rect.x -= delta_x #-
            self.rect.y -= delta_y #-
        elif 180 <= self.phi < 270:
            self.rect.x -= delta_x #-
            self.rect.y += delta_y #+
        elif 270 <= self.phi < 360:
            self.rect.x += delta_x #+
            self.rect.y += delta_y #+

        self.vision.center = self.rect.center