from pico2d import *
from share import game_framework
from valleyball.player_state_machine import *

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

def time_out(e):
    return e[0] == 'TIME_OUT'



class p1_state_machine:
    def __init__(self, bp1):
        self.bp1 = bp1
        self.cur_state = idle
        self.table = {
            idle: {d_down:run_right,a_down:run_left,w_down:jump},
            jump: {time_out:run_down},
            run_right:{d_down:run_right ,d_up:idle,a_down:run_left,w_down:jump},
            run_left: {a_down:run_left ,a_up:idle,d_down:run_right,w_down:jump},
            run_down:{time_out:idle}
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
        self.state_machine = p1_state_machine(self)
        self.state_machine.start()
        self.dir = 'right'
        self.score = 0
        self.run_speed=300
        self.jump_speed=300

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def render(self):
        self.state_machine.render()

    def get_bb(self):
            return self.x - 60, self.y - 90, self.x - 59.9, self.y + 60

    def handle_collusion(self, group, other):
        pass