import tennis.balley_player1
import tennis.game_world
# from tennis import game_framework, balley_player1
from tennis.background import *
from pico2d import *
from tennis.game_framework import *

def handle_events():
    global mx,my
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            tennis.game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass
        else:
            p1.handle_event(event)



def init():
    global p1
    p1= balley_player1.bplayer1()
    game_world.addobject(p1, 1)
    bg=background()
    game_world.addobject(bg)
    ###############################


def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    # draw_rectangle(340,300,880,430)
    # draw_rectangle(340,130,880,260)
    update_canvas()

def pause():
    pass

def resume():
    pass

def finish():
    game_world.clear()
    pass