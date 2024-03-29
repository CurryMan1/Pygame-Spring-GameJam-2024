import pygame
import random
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

        self.player = Player(app)

    def handle_event(self, event):
        ...

    def draw(self):
        self.app.screen.fill(DARK_GREY)
        self.title.draw()

        self.player.draw()

    def update(self, delta):
        self.player.update(delta)

