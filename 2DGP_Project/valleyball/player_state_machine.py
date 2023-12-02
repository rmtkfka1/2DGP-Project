from pico2d import *


from share import game_framework
from valleyball.balley_2player_mode import *

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
        player.dir='right'
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

        if player.y >120 and player.down==True:
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
        player.frame = 0

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if (player.x <570):
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
        if (player.x >0):
            player.x -= player.run_speed * game_framework.frame_time


    @staticmethod
    def render(player):
        player.run_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class smash:
    @staticmethod
    def enter(player, e):
        player.frame=0
        player.cur_state = 'smash'
    @staticmethod
    def exit(player, e):
        player.dir='right'

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
            player.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def render(player):
        player.smash_right_image.clip_draw(int(player.frame) * 64, 0, 64, 93, player.x, player.y)
        pass

class slide_right:
    @staticmethod
    def enter(player, e):
        player.down = False
        player.cur_state ='slide_right'
        player.frame=0
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.dir='right'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        if (player.x < 600 and player.x >590):
            player.state_machine.handle_event(('TIME_OUT', 0))

        if (player.x < 600):
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
        player.cur_state ='slide_left'
        player.frame=15
        player.dist =0
    @staticmethod
    def exit(player, e):
        player.dir='left'
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame - FRAMES_PER_SLIDE * ACTION_PER_SLIDE * game_framework.frame_time) % 15

        if (player.x < 10 and player.x >0):
            player.state_machine.handle_event(('TIME_OUT', 0))

        if (player.x > 0):
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
        player.dir ='right'
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


