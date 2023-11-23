from share import game_world, game_framework
from tennis.PointSystem import PointSystem
from tennis.audience import Audience
from tennis.ball import Ball
from tennis.flag import Flag
from tennis.player1 import *
from tennis.player2 import *
from tennis.background import *
from pico2d import *

from tennis.referee import referee


def handle_events():
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        else:
            p1.handle_event(event)
            p2.handle_event(event)


def init():
    global p1
    global p2
    global bg
    global myball
    global ps

    p1 = player1()
    p2 = player2()
    bg = background()
    seat_front= chair(530,370)
    seat_middle = chair(550, 420)
    seat_last = chair(570, 470)
    bar =  safe_bar()
    myball = Ball()
    ref = referee(myball)
    flag =Flag()
    ps =PointSystem(myball,p1,p2)
    audience=Audience(myball,80,355)
    audience_middle=Audience(myball,100,400)
    audience_last = Audience(myball, 125, 445)

    game_world.addobject(ps, 10)
    game_world.addobject(bg, 0)
    game_world.addobject(audience, 7)
    game_world.addobject(seat_front, 6)
    game_world.addobject(audience_middle, 5)
    game_world.addobject(seat_middle, 4)
    game_world.addobject(audience_last, 3)
    game_world.addobject(seat_last, 2)

    game_world.addobject(flag, 1)

    game_world.addobject(bar, 7)
    game_world.addobject(myball, 9)
    game_world.addobject(p1, 8)
    game_world.addobject(p2, 8)
    game_world.addobject(ref, 1)

    game_world.add_collusion_pair("player1:ball", p1, myball)
    game_world.add_collusion_pair("player2:ball", p2, myball)



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
