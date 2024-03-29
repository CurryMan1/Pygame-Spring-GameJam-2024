import pygame
import random
from src.buttons.text_button import TextButton
from src.constants import BLACK, WIDTH
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

    def handle_event(self, event):
        ...

    def draw(self):
        self.app.screen.fill(BLACK)
        self.title.draw()

    def update(self, delta):
        ...

    def draw_grid(self):
        ...
