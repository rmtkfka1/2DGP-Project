import game_world
import play_mode
from audience import Audience
from ball import Ball
from flag import Flag
from player1 import *
from player2 import *
from background import *
from pico2d import *

from referee import referee



def handle_events():
    global mx,my
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if mx > 340 and mx< 880 and my>130 and my<260:
                game_framework.change_mode(play_mode)
        else:
            p1.handle_event(event)
            p2.handle_event(event)


def init():
    global running
    global p1
    global p2
    global ball

    running = True
    layer1 = p1_layer()
    layer2 = p2_layer()
    myui = ui()


    p1 = player1()
    p2 = player2()
    bg = background()
    seat_front = chair(530, 370)
    seat_middle = chair(550, 420)
    seat_last = chair(570, 470)
    bar = safe_bar()
    myball = Ball()
    myball.start = True
    ref = referee(myball)
    flag = Flag()
    audience = Audience(myball, 80, 355)
    audience_middle = Audience(myball, 100, 400)
    audience_last = Audience(myball, 125, 445)

    game_world.addobject(bg, 0)
    game_world.addobject(audience, 7)
    game_world.addobject(seat_front, 6)
    game_world.addobject(audience_middle, 5)
    game_world.addobject(seat_middle, 4)
    game_world.addobject(audience_last, 3)
    game_world.addobject(seat_last, 2)

    game_world.addobject(flag, 1)
    game_world.addobject(bar, 7)
    game_world.addobject(p1, 8)
    game_world.addobject(p2, 8)
    game_world.addobject(ref, 1)
    game_world.addobject(layer1, 10)
    game_world.addobject(layer2, 10)

    game_world.addobject(myui, 10)


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