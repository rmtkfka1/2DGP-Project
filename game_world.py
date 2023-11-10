from player1 import *
from player2 import *
from background import *
from pico2d import *


world=[[],[],[],[],[]]

collusion_world = {}

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

def remove_collusion_object(o):
    for pairs in collusion_world.value():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collusion_object(o)
            del o
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

def add_collusion_pair(group,a,b):
    if group not in collusion_world:
        print(f"new group {group} added ")
        collusion_world[group]=[[],[]]
    if a:
        collusion_world[group][0].append(a)
        collusion_world[group][1].append(b)


def handle_collusions():
    for group , pairs in collusion_world.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a,b):
                    a.handle_collusion(group,b)
                    b.handle_collusion(group,a)

