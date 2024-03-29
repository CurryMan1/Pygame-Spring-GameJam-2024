import pygame
import math
from src.constants import RED
from src.utils import load_img
class Feet():
    def __init__(self, player, app, distance):
        self.timer = 0
        self.app = app
        self.player = player
        self.distance = distance
        self.image = pygame.image.load("assets/player_assets/cold/player_feet_c.png")
        self.image = pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_frect(center=(self.player.rect.x + self.distance, self.player.rect.y + 110))

    def update(self, d):
        self.timer += d * 20
        print(self.timer * 10)
        if self.player.vel.x > 0:
            runx = math.cos(self.timer) * self.player.vel.x * 4
            runy = math.sin(self.timer) * self.player.vel.x * 4
        elif self.player.vel.x < 0:
            runx = math.sin(self.timer) * self.player.vel.x * 4
            runy = math.cos(self.timer) * self.player.vel.x * 4
        else:
            runx = 0
            runy= 0
        self.rect.x = self.player.rect.x + self.distance - self.player.vel.x * 10 + runx
        self.rect.y = self.player.rect.y + 100 + self.player.vel.y * 10 + runy

    def draw(self):
        self.app.screen.blit(self.image, self.rect)