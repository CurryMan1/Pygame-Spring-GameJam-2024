import pygame
from src.constants import BLACK


class ImageButton:
    def __init__(self, app, surf: pygame.surface.Surface, selected_surf=None, **kwargs):
        self.app = app
        self.surf = surf
        self.selected_surf = selected_surf
        self.shadow = surf.copy()
        self.shadow.fill(BLACK, special_flags=pygame.BLEND_RGB_MULT)

        self.rect = self.surf.get_rect(**kwargs)
        self.hovered = False

    def is_clicked(self) -> bool:
        self.hovered = self.rect.collidepoint(self.app.mouse_pos)
        return self.hovered and self.app.mouse_input[0]

    def draw(self) -> None:
        self.app.screen.blit(self.shadow, self.rect.move(10, 10))
        if self.hovered and self.selected_surf:
            self.app.screen.blit(self.selected_surf, self.rect)
        else:
            self.app.screen.blit(self.surf, self.rect)
