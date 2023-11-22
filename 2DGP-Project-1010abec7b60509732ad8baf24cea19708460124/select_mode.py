import balley_mode
import game_world
import play_mode
import tennis_mode
from audience import Audience
from ball import Ball
from flag import Flag
from player1 import *
from player2 import *
from background import *
from pico2d import *

from referee import referee





def handle_events():
    global mx, my
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if mx > 350 and mx < 1000 and my > 220+150 and my <  280+150:
                game_framework.change_mode(balley_mode)
            if mx > 350 and mx < 900 and my > 220 and my < 280:
                game_framework.change_mode(tennis_mode)
        else:
            pass



def init():
    global  font
    font = load_font('monogram.TTF', 100)
    bg = select_background()
    game_world.addobject(bg, 5)

    pass


def update():

    game_world.update()


def draw():
    global font

    clear_canvas()
    game_world.render()
    font.draw(350, 400, f'mode: valleyball', (255, 255, 255))
    font.draw(350, 250, f'mode: Tennis', (255, 255, 255))
    draw_rectangle(350, 220+150, 1000, 280+150) ## 배구
    draw_rectangle(350,220,900,280) ## 테니스

    update_canvas()



def pause():
    pass


def resume():
    pass


def finish():
    game_world.clear()
    pass