import game_world
import play_mode
from ball import Ball
from player1 import *
from player2 import *
from background import *
from pico2d import *



def handle_events():
    global mx,my
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            game_framework.running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 700 - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if mx > 340 and mx< 880 and my>130 and my<260:
                game_framework.change_mode(play_mode)
        else:
            p1.handle_event(event)
            p2.handle_event(event)


def init():
    global running
    global p1
    global p2
    global ball

    running = True

    bg =background()
    seat = chair()
    bar =safe_bar()
    ball=Ball()
    ball.start=True
    layer1 = p1_layer()
    layer2 = p2_layer()
    myui = ui()
    mylogo =logo()
    p1=player1()
    p2=player2()

    game_world.addobject(bg,0)
    game_world.addobject(seat,1)
    ##관중 2번 에다가 추가하면됨
    game_world.addobject(bar,3)

    game_world.addobject(layer1,4)
    game_world.addobject(layer2,4)

    game_world.addobject(myui,4)
    game_world.addobject(ball,3)

    game_world.addobject(p1,3)
    game_world.addobject(p2,3)
    game_world.addobject(mylogo,4)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    # draw_rectangle(340,300,880,430)
    # draw_rectangle(340,130,880,260)
    update_canvas()




def pause():
    pass

def resume():
    pass

def finish():
    game_world.clear()
    pass