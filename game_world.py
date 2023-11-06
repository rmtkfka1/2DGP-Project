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