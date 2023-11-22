from pico2d import *

from balley_state_machine import *

def spacedown(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def time_out(e):
    return e[0] == 'TIME_OUT'


class idle:
    @staticmethod
    def enter(player, e):
        player.gravity = 0.05


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = ( player.frame +ACTION_PER_TIME*FRAMES_PER_ACTION * game_framework.frame_time)%6


    @staticmethod
    def render(player):
        player.image.clip_draw(int(player.frame)*64,0,64,86,player.x,player.y)
        pass


class jump:
    @staticmethod
    def enter(player, e):
        player.wait_time =get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):

        if(player.frame < 5):
            player.frame += (ACTION_PER_TIME * 2*FRAMES_PER_ACTION * game_framework.frame_time)


        if(player.y <600):
            player.y += 500 * game_framework.frame_time

        if(get_time()- player.wait_time>0.3):
            player.state_machine.handle_event(('TIME_OUT',0))

        player.top = player.y + 90
        player.bottom = player.y - 60

    @staticmethod
    def render(player):
        player.image.clip_draw(int(player.frame)*115,0,115,175,player.x,player.y)
        pass


class bp1_state_machine:
    def __init__(self, bp1):
        self.bp1 = bp1
        self.cur_state = idle
        self.table = {
            idle: {spacedown: jump},
            jump: {spacedown: jump, time_out: idle}
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


class bplayer1:
    def __init__(self):
        self.x = 400
        self.y = 120
        self.frame = 0
        self.image = load_image('resource/balley/test.png')
        self.state_machine = bp1_state_machine(self)
        self.state_machine.start()
        self.score = 0

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