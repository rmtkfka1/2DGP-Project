from pico2d import *

import share.game_framework
import share.game_world
from tennis import tennis_1player_mode, tennis_2player_mode


# Game object class here


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            share.game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            share.game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_e:
            share.game_framework.pop_mode()




def init():
    global pannel
    pannel = Pannel()
    share.game_world.addobject(pannel,10)


def update():
    share.game_world.update()


def draw():
    clear_canvas()
    share.game_world.render()
    update_canvas()


def finish():
    share.game_world.remove_object(pannel)


class Pannel:
    def __init__(self):
        self.image = load_image('resource/testing.png')
        self.font  = load_font('resource/monogram.TTF',80)
    def render(self):
        self.image.draw(600, 350)
        self.font.draw(360, 200+150, f'Player1 JUMP : UP', (255, 0, 0))
        self.font.draw(360, 150+150, f'Player2 JUMP : W', (255, 0, 0))
        self.font.draw(360, 100+150, f'Press E to Return', (255, 0, 0))
        # self.font.draw(480, 200, f'Press ESC to end', (255, 255, 255))
    def update(self):
        pass