import pygame
from src.constants import BLOCK_PROPERTIES


class Tile:
    def __init__(self, pos, surface, tag: str):
        self.accel, self.friction, self.max_speed = BLOCK_PROPERTIES[tag]

        self.surf = surface
        self.rect = self.surf.get_rect(topleft=pos)

