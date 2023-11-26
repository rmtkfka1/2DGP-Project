import valleyball.ball
from share import game_world, game_framework
from tennis.background import *
from pico2d import *

from valleyball import Player1
from valleyball import Net
from valleyball import player_ai

p1=None

def handle_events():
    global mx, my
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            pass
        else:
            p1.handle_event(event)


def init():
    global p1
    p1 = Player1.player1()
    bg = background()
    ball=valleyball.ball.Ball()
    net = valleyball.Net.net()
    ai= valleyball.player_ai.ai(ball)
    ###############################
    game_world.addobject(p1, 1)
    game_world.addobject(bg)
    game_world.addobject(ball)
    game_world.addobject(net)
    game_world.addobject(ai)


    game_world.add_collusion_pair("player1:ball", p1, ball)
    game_world.add_collusion_pair("net:ball", net, ball)
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
