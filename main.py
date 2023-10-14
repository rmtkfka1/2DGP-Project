from pico2d import *
from player1 import *


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        else :
            p1.handle_event(event)

def reset_world():
    global running
    global world
    global p1

    world=[]
    running = True
    p1=player1()
    world.append(p1)

def update_world():

    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.render()
    update_canvas()

open_canvas(1250, 700)
reset_world()

while(running):
    handle_events()
    update_world()
    render_world()
    delay(0.01)

