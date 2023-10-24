from player1 import *
from player2 import *
from background import *
from pico2d import *


world=[]

def addobject(o):
    world.append(o)

def update():
    for o in world:
        o.update()


def render():
    for o in world:
        o.render()


def remove_object():
    for o in world:
        world.remove(o)
        return
    raise ValueError('없는데왜 지울려고해 미친놈아')
