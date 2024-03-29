import pygame
from src.constants import WIDTH, HEIGHT, BLUE, GRAVITY


class Player:
    max_speed = 2
    accel = 10
    JUMP_POWER = 100

    def __init__(self, app):
        self.app = app

        self.image = pygame.Surface((100, 100))
        self.image.fill(BLUE)
        self.rect = self.image.get_frect(center=(WIDTH/2, HEIGHT/2))

        self.vel = pygame.Vector2(0, 0)
        self.x_direction = 0

        self.standing_block = None

    def draw(self):
        self.app.screen.blit(self.image, self.rect)

    def update(self, delta):
        self.x_direction = 0
        if self.app.keys[pygame.K_a]:
            self.x_direction -= 1
        if self.app.keys[pygame.K_d]:
            self.x_direction += 1

        self.rect.center += self.vel * 0.5

        if self.x_direction == 0:
            #TEMPORARY
            friction = 7.5
            fd = friction*delta #use the friction of STANDING BLCOK
            if abs(self.vel.x) > fd:
                self.vel.x -= self.vel.x * fd
            else:
                self.vel.x = 0
        else:
            self.vel.x = min(
                self.vel.x + (self.x_direction * self.accel * delta),
                self.x_direction*self.max_speed,
                key=abs
            )

        self.rect.center += self.vel*0.5
