from pico2d import *
from share import game_framework
from valleyball.player_ai import run_right_to_middle, run_left_to_middle
from valleyball.player_state_machine import *

def w_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP

def time_out(e):
    return e[0] == 'TIME_OUT'

def d_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def d_up(e):

    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT

def a_down(e):

    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT

def a_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def s_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN
def s_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def time_out(e):
    return e[0] == 'TIME_OUT'

def f_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_k


from pico2d import *


from share import game_framework
from valleyball.balley_mode import *

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12

TIME_PER_ACTION_SMASH =1.2
ACTION_PER_SMASH = 1.0 / TIME_PER_ACTION_SMASH
FRAMES_PER_SMASH = 13

TIME_PER_ACTION_SLIDE =0.7
ACTION_PER_SLIDE = 1.0 / TIME_PER_ACTION_SLIDE
FRAMES_PER_SLIDE = 15


TIME_PER_ACTION_RECEPTION = 1.0
ACTION_PER_RECEPTION = 1.0 / TIME_PER_ACTION_RECEPTION
FRAMES_PER_RECEPTION = 11

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class idle:
    @staticmethod
    def enter(player, e):
        player.cur_state ='idle'
        player.frame = 0
        pass

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

    @staticmethod
    def render(player):
        if player.dir =='left':
            player.idle_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        if player.dir == 'right':
            player.idle_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class jump:
    @staticmethod
    def enter(player, e):
        player.down=False
        player.cur_state ='jump'
        player.frame = 0
        pass


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12


        if (player.y < 400 and player.down ==False):
            player.y += player.jump_speed * game_framework.frame_time

        if(player.y>400):
            player.y=400
            player.down=True

        if player.down==True:
            player.y -= player.jump_speed * game_framework.frame_time



        if player.y<120:
            player.state_machine.handle_event(('TIME_OUT',0))

    @staticmethod
    def render(player):
        if player.dir == 'left':
            player.idle_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        if player.dir == 'right':
            player.idle_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass

class run_right:
    @staticmethod
    def enter(player, e):
        player.dir = 'right'
        player.cur_state = 'run_right'
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12


        if (player.x < 1200):
            player.x += player.run_speed * game_framework.frame_time

    @staticmethod
    def render(player):
        player.run_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_left:
    @staticmethod
    def enter(player, e):
        player.dir='left'
        player.cur_state ='run_left'
        player.frame = 0
    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if (player.x >650):
            player.x -= player.run_speed * game_framework.frame_time


    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_left_to_middle:
    @staticmethod
    def enter(player, e):
        player.dir='left'
        player.cur_state ='run_left_to_middle'
        player.frame = 0
    @staticmethod
    def exit(player, e):


        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.x -= player.run_speed * game_framework.frame_time

        if (player.x<900):
            player.x = 900
            player.state_machine.handle_event(('TIME_OUT', 0))



    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_right_to_middle:
    @staticmethod
    def enter(player, e):
        player.dir = 'left'
        player.cur_state = 'run_right_to_middle'
        player.frame = 0

    @staticmethod
    def exit(player, e):

        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        player.x += player.run_speed * game_framework.frame_time

        if (player.x>900):
            player.x=900
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def render(player):
        player.run_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class smash:
    @staticmethod
    def enter(player, e):
        player.frame=0
        player.cur_state = 'smash'
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.dir='left'
        player.frame = 0
        player.dist =0

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_SMASH * ACTION_PER_SMASH * game_framework.frame_time) % 13


        if (player.y < 400 and player.down == False):
            player.y += player.jump_speed * game_framework.frame_time

        if (player.y > 400):
            player.y = 400
            player.down = True

        if player.y > 120 and player.down == True:
            player.y -= player.jump_speed * game_framework.frame_time

        if player.y < 120:
            player.y=120
            player.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def render(player):
        player.smash_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass

class slide_right:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.job =True
        player.cur_state ='slide_right'
        player.frame=0
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.frame = 0
        player.job =False
        player.dist =0
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15


        if (player.x < 1200 and player.x >1170):
            player.state_machine.handle_event(('TIME_OUT', 0))

        if (player.x < 1200):
            player.x += player.slide_speed * game_framework.frame_time
            player.dist += 30* game_framework.frame_time

        if player.dist >20:
            player.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def render(player):
        player.slide_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass



class slide_left:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.job =True
        player.cur_state ='slide_left'
        player.frame=15
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.job =False
        player.dist = 0
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        if (player.x < 650 and player.x > 610):
            player.state_machine.handle_event(('TIME_OUT', 0))

        if (player.x > 600):
            player.x -= player.slide_speed * game_framework.frame_time
            player.dist += 30* game_framework.frame_time

        if player.dist >20:
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def render(player):
        player.slide_left_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass


class reception:
    @staticmethod
    def enter(player, e):
        player.wait_time = get_time()
        player.down = False
        player.dir ='left'
        player.cur_state ='reception'
        player.frame=0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_RECEPTION * ACTION_PER_RECEPTION * game_framework.frame_time) % 11

        if (get_time() - player.wait_time > 1.0):
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def render(player):
        player.reception_right_image.clip_draw(int(player.frame) * 70, 0, 70, 93, player.x, player.y)
        pass

class p2_state_machine:
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


class player2:
    def __init__(self):
        self.x = 1000
        self.y = 120
        self.frame = 0
        self.idle_left_image = load_image('resource/balley/ai_idle_left.png')
        self.idle_right_image = load_image('resource/balley/ai_idle_right.png')
        self.run_right_image = load_image('resource/balley/ai_right_run.png')
        self.run_left_image = load_image('resource/balley/ai_left_run.png')
        self.smash_right_image = load_image('resource/balley/ai_smash.png')
        self.slide_right_image = load_image('resource/balley/ai_slide_right.png')
        self.slide_left_image = load_image('resource/balley/ai_left_slide.png')
        self.reception_right_image = load_image('resource/balley/ai_reception.png')
        self.cur_state = idle
        self.dir = 'left'
        self.score = 0
        self.down = False

        self.run_speed = 300
        self.jump_speed = 500
        self.slide_speed = 400
        self.dist = 0
        self.stop =False
        self.count = 0
        self.job = False
        self.state_machine = p2_state_machine(self)
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