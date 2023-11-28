from pico2d import *
from share import game_framework
from valleyball.player_ai import run_right_to_middle, run_left_to_middle
from valleyball.player_state_machine import *
from valleyball.balley_mode import *


def w_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w

def time_out(e):
    return e[0] == 'TIME_OUT'

def d_down(e):

    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d

def d_up(e):

    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d

def a_down(e):

    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a

def s_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s
def s_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s


def time_out(e):
    return e[0] == 'TIME_OUT'

def f_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_f



class p1_state_machine:
    def __init__(self, bp1):
        self.bp1 = bp1
        self.cur_state=bp1.cur_state
        self.table = {
            idle: {d_down:run_right,a_down:run_left,w_down:jump,s_down: reception},
            jump: {time_out:idle, f_down:smash },
            run_right:{d_down:run_right ,d_up:idle,a_down:run_left,w_down:jump,f_down:slide_right,s_down: reception},
            run_left: {a_down:run_left ,a_up:idle,d_down:run_right,w_down:jump,f_down:slide_left,s_down:reception},
            smash:{ time_out:idle},
            slide_right:{time_out:idle},
            slide_left:{time_out:idle},
            reception:{time_out:idle},
        }

    def start(self):
        self.cur_state.enter(self.bp1, ('start', 0))

    def update(self):
        self.cur_state.update(self.bp1)

    def render(self):
        self.cur_state.render(self.bp1)

    def handle_event(self, e):
        for check_event, next_state in self.table[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.bp1, e)
                self.cur_state = next_state
                self.cur_state.enter(self.bp1, e)
                return True
        return False


class player1:
    def __init__(self):
        self.x = 400
        self.y = 120
        self.frame = 0
        self.idle_left_image = load_image('resource/balley/idle_left.png')
        self.idle_right_image = load_image('resource/balley/idle_right.png')
        self.run_right_image = load_image('resource/balley/playerRun_right.png')
        self.run_left_image = load_image('resource/balley/playerRun_left.png')
        self.smash_right_image = load_image('resource/balley/playerSmash_right2.png')
        self.slide_right_image = load_image('resource/balley/playerSlide_right.png')
        self.slide_left_image = load_image('resource/balley/playerSlide_left.png')
        self.reception_right_image = load_image('resource/balley/playerReception.png')
        self.cur_state = idle
        self.dir = 'right'
        self.score = 0
        self.run_speed=300
        self.jump_speed=500
        self.slide_speed=400
        self.counting=0
        self.state_machine = p1_state_machine(self)
        self.state_machine.start()




    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()
        draw_rectangle(*self.get_bb())

    def get_bb(self):
            return self.x - 20, self.y - 60, self.x +20, self.y + 50

    def handle_collusion(self, group, other):
        pass