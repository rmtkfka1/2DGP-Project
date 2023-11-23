from pico2d import *

import share.game_framework
import share.game_world



# Game object class here


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            share.game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            share.game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            share.game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            share.game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
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

    def render(self):
        self.image.draw(400, 300)

    def update(self):
        pass