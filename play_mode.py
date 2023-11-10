import game_world
from ball import Ball
from player1 import *
from player2 import *
from background import *
from pico2d import *


def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        else:
            p1.handle_event(event)
            p2.handle_event(event)


def init():
    global running
    global p1
    global p2
    global bg
    global ball

    running = True
    p1 = player1()
    p2 = player2()
    bg = background()
    seat = chair()
    bar =  safe_bar()
    ball = Ball()


    game_world.addobject(bg, 0)

    game_world.addobject(ball, 2)

    game_world.addobject(seat, 1)
    #2번 레이어 에 관중추가


    game_world.addobject(bar, 3)
    game_world.addobject(p1, 3)
    game_world.addobject(p2, 3)

    game_world.add_collusion_pair("player1:ball", p1, ball)
    game_world.add_collusion_pair("player2:ball", p2, ball)


def update():
    game_world.update()

    game_world.handle_collusions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass


def finish():
    game_world.clear()
    pass
