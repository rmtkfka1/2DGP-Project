from player1 import *
from player2 import *
from background import *
from pico2d import *


world=[[],[],[],[]]

def addobject(o,depth=0):
    world[depth].append(o)

def addobjects(o,depth=0):
    world[depth] += o


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.render()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')

def clear():
    for layer in world:
        layer.clear()


def collide(a,b):
    la,ba,ra,ta =a.get_bb()
    lb,bb,rb,tb =b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

def reflection_vector(x,y,nx,ny):
    new_x = x + 2 * nx * ((-x * nx + -y * ny))
    new_y = y + 2 * ny * ((-x * nx + -y * ny))
    return new_x,new_y