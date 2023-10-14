from pico2d import *

open_canvas(1250,700)


class player1:
    def __init__(self):
        self.x=1100
        self.y=100
        self.frame = 0
        self.image = load_image('1.png')
    def update(self):
        self.frame=(self.frame+1)%5
        delay(0.05)
    def render(self):
        self.image.clip_draw(self.frame*40,0,40,40,self.x,self.y,200,200)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.key == SDLK_ESCAPE:
            running = False
        else:
            pass

def reset_world():
    global running
    global world
    running = True
    world = []  #월드 리스트안에 객체들을 담을예정
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

reset_world()

while(running):
    handle_events()
    update_world()
    render_world()




