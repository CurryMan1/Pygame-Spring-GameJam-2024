import pygame
from src.scene_enum import Scenes
from src.scenes.base import BaseScene
from src.buttons.text_button import TextButton
from src.constants import WIDTH, HEIGHT, DARK_GREY


class Start(BaseScene):
    def __init__(self, app):
        super().__init__(app)

        self.title = TextButton(
            self.app,
            'Game??',
            self.app.title_font,
            center=(WIDTH/2, 300)
        )

        self.start_btn = TextButton(
            self.app,
            'Start',
            self.app.normal_font,
            center=(WIDTH/2, 520)
        )

        self.settings_btn = TextButton(
            self.app,
            'Settings',
            self.app.normal_font,
            center=(WIDTH/2, 660)
        )

        self.quit_btn = TextButton(
            self.app,
            'Quit',
            self.app.normal_font,
            center=(WIDTH/2, 800)
        )

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.stop()

    def update(self, delta):
        if not self.app.mouse_clicked[0]:
            if self.start_btn.is_clicked():
                self.app.change_scene(Scenes.GAME)

            if self.settings_btn.is_clicked():
                ...

            if self.quit_btn.is_clicked():
                self.app.stop()

    def draw(self):
        self.app.screen.fill(DARK_GREY)

        self.title.draw()

        self.start_btn.draw()
        self.settings_btn.draw()
        self.quit_btn.draw()
