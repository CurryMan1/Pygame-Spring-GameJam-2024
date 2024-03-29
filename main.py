import pygame
from src.utils import load_img
from src.constants import WIN_SIZE
from src.scene_enum import Scenes
from src.scenes.start import Start
from src.scenes.game import Game


class App:
    FONT = 'assets/fonts/mouldy_cheese.ttf'

    def __init__(self):
        pygame.init()

        #display
        self.screen = pygame.display.set_mode(WIN_SIZE, pygame.SCALED | pygame.FULLSCREEN)
        pygame.display.set_caption('Game')
        #pygame.display.set_icon(load_img('icon.png', True))

        #clock
        self.clock = pygame.time.Clock()

        #font
        self.title_font = pygame.font.Font(self.FONT, 150)
        self.normal_font = pygame.font.Font(self.FONT, 70)

        #states
        self.scenes = {
            Scenes.START: Start(self),
            Scenes.GAME: Game(self)
        }

        self.current_scene = self.scenes[Scenes.START]

        #game vars
        self.running = True
        self.restart = False
        self.delta = 0
        self.mouse_pos = ()
        self.mouse_input = ()

        self.clicked = [False]*3

    def run(self):
        while self.running:
            self.delta = min(self.clock.tick()/1000, 0.1)

            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_input = pygame.mouse.get_pressed()

            #update and draw state
            self.current_scene.update(self.delta)
            self.current_scene.draw()

            if self.mouse_input[0]:
                self.clicked[0] = True
            else:
                self.clicked[0] = False

            #handle events
            for event in pygame.event.get():
                self.current_scene.handle_event(event)
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

    def change_scene(self, scene):
        self.clicked[0] = True
        self.current_scene = self.scenes[scene]

    def stop(self):
        self.running = False


if __name__ == '__main__':
    app = App()
    app.run()
    pygame.quit()
