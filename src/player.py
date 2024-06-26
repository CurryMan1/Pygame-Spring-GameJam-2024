import pygame
from src.feet import Feet
from src.constants import WIDTH, HEIGHT, BLUE, GRAVITY


class Player:
    JUMP_POWER = 100
    def __init__(self, app):
        self.app = app

        self.image = pygame.Surface((100, 100))
        self.image.fill(BLUE)
        self.rect = self.image.get_frect(center=(WIDTH/2, HEIGHT/2))

        self.vel = pygame.Vector2(0, 0)
        self.x_direction = 0
        self.feet = Feet(self,self.app,-10)
        self.feet1 = Feet(self, self.app,90)

        self.standing_block = None

    def draw(self):
        self.app.screen.blit(self.image, self.rect)
        self.feet.draw()
        self.feet1.draw()

    def update(self, delta):
        #temp
        max_speed = 2
        accel = 10
        friction = 7.5

        self.x_direction = 0
        if self.app.keys[pygame.K_a]:
            self.x_direction -= 1
        if self.app.keys[pygame.K_d]:
            self.x_direction += 1

        self.rect.center += self.vel * 0.5

        if self.x_direction == 0:
            fd = friction*delta #use the friction of STANDING BLCOK
            if abs(self.vel.x) > fd:
                self.vel.x -= self.vel.x * fd
            else:
                self.vel.x = 0
        else:
            self.vel.x = min(
                self.vel.x + (self.x_direction*accel*delta),
                self.x_direction*max_speed,
                key=abs
            )

        self.rect.center += self.vel*0.5
        self.feet.update(delta)
        self.feet1.update(delta)
