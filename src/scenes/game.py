import pygame
import random
from pytmx.util_pygame import load_pygame
from src.utils import load_tmx_objects
from src.player import Player
from src.buttons.text_button import TextButton
from src.constants import DARK_GREY, WIDTH
from src.scene_enum import Scenes
from src.scenes.base import BaseScene


class Game(BaseScene):
    def __init__(self, app):
        super().__init__(app)

        self.title = TextButton(
            self.app,
            'Game',
            self.app.title_font,
            center=(WIDTH/2, 150)
        )

        loaded_tmx_data = load_pygame("assets/maps/temperaturegame_map_test.tmx")
        self.liquid_blocks = load_tmx_objects(loaded_tmx_data, ['water', 'lava'])
        self.normal_blocks = load_tmx_objects(loaded_tmx_data, ['stone', 'wood'])
        self.ice_blocks = load_tmx_objects(loaded_tmx_data, ['ice'])

        self.player = Player(app)

    def handle_event(self, event):
        ...

    def draw(self):
        self.app.screen.fill(DARK_GREY)
        self.title.draw()

        self.player.draw()

    def update(self, delta):
        self.player.update(delta)

    def update_lvl_info(self, level: int):
        ...
