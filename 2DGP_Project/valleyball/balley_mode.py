import valleyball.ball
from share import game_world, game_framework
from tennis.audience import Audience
from tennis.background import *
from pico2d import *

from tennis.flag import Flag
from tennis.referee import referee
from valleyball import Player2
from valleyball import Player1
from valleyball import Net
from valleyball import PointSystem
from valleyball import player_ai
import valleyball.server


p1=None

def handle_events():
    global mx, my # Declare owner as a global variable here
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass
        else:
            if(valleyball.server.stop_contorl==False):
                p1.handle_event(event)
                p2.handle_event(event)

def init():
    global p1
    global p2
    p1 = Player1.player1()
    bg = background()
    ball=valleyball.ball.Ball()
    net = valleyball.Net.net()
    # ai= valleyball.player_ai.ai(ball)
    p2 =Player2.player2()
    ps =PointSystem.PointSystem(ball,p1,p2)


    ###############################
    game_world.addobject(p1, 10)
    game_world.addobject(bg)
    game_world.addobject(ball,10)
    game_world.addobject(net,9)
    game_world.addobject(p2,10)
    # game_world.addobject(ai)

    seat_front = chair(530, 370)
    seat_middle = chair(550, 420)
    seat_last = chair(570, 470)
    bar = safe_bar()
    ref = referee(ball)
    flag = Flag()
    audience = Audience(ball, 80, 355)
    audience_middle = Audience(ball, 100, 400)
    audience_last = Audience(ball, 125, 445)

    game_world.addobject(audience, 7)
    game_world.addobject(seat_front, 6)
    game_world.addobject(audience_middle, 5)
    game_world.addobject(seat_middle, 4)
    game_world.addobject(audience_last, 3)
    game_world.addobject(seat_last, 2)
    game_world.addobject(flag, 1)
    game_world.addobject(bar, 7)
    game_world.addobject(ref, 1)
    game_world.addobject(ps,10)



    game_world.add_collusion_pair("player1:ball", p1, ball)
    game_world.add_collusion_pair("net:ball", net, ball)
    game_world.add_collusion_pair("player2:ball", p2, ball)

    # game_world.add_collusion_pair("ai:ball", ai, ball)



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
