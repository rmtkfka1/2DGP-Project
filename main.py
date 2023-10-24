import game_world
from player1 import *
from player2 import *
from background import *
from pico2d import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        else :
            p1.handle_event(event)
            p2.handle_event(event)


def create_world():
    global running
    global p1
    global p2
    global bg

    running = True
    p1 = player1()
    p2 = player2()
    bg =background()

    game_world.addobject(bg)
    game_world.addobject(p1)
    game_world.addobject(p2)



def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas(1200, 700)
create_world()

while(running):
    handle_events()
    update_world()
    render_world()
    delay(0.05)

