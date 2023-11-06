from pico2d import *

import game_framework
from player_state_machine import idle, jump


def spacedown(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key ==SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'


class p1_state_machine:
    def __init__(self, p1):
        self.p1 =p1
        self.cur_state=idle
        self.table={
            idle: {spacedown : jump },
            jump: {spacedown : jump ,time_out:idle}
        }
    def start(self):
        self.cur_state.enter(self.p1,('start',0))
    def update(self):
        self.cur_state.update(self.p1)
    def render(self):
        self.cur_state.render(self.p1)



    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.p1, e)
                self.cur_state = next_state
                self.cur_state.enter(self.p1, e)
                return True
        return False

class player1:
    def __init__(self):
        self.x=1000
        self.y=180
        self.frame = 0
        self.frame_divide=0.0
        self.image = load_image('resource/p1_img.png')
        self.state_machine=p1_state_machine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def handle_event(self,event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        cur_state = self.state_machine.cur_state
        if cur_state == idle:
            return self.x-60,self.y-90,self.x-15,self.y+60
        if cur_state == jump:
            return self.x-60, self.y -60, self.x -15, self.y + 90




