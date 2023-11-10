import game_world
import play_mode
from ball import Ball
from player1 import *
from player2 import *
from background import *
from pico2d import *



def handle_events():
    global mx,my
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if mx > 360 and mx< 900 and my>140 and my<280:
                game_framework.change_mode(play_mode)



def init():
    global running
    global p1
    global p2
    global ball

    running = True

    bg =background_start()
    ball=Ball()

    game_world.addobject(bg,0)
    game_world.addobject(ball,2)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    # draw_rectangle(360,300,890,430)
    # draw_rectangle(360,140,900,280)
    update_canvas()




def pause():
    pass

def resume():
    pass

def finish():
    game_world.clear()
    pass