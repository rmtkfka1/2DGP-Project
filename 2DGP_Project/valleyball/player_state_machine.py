from pico2d import get_time
from share import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class idle:
    @staticmethod
    def enter(player, e):
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
        pass


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        if (player.y < 250):
            player.y += player.jump_speed * game_framework.frame_time

        if(player.y>250):
            player.y=250
            player.state_machine.handle_event(('TIME_OUT', 0))

        pass
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

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12
        if (player.x <600):
            player.x += player.run_speed * game_framework.frame_time

    @staticmethod
    def render(player):
        player.run_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        pass


class run_left:
    @staticmethod
    def enter(player, e):
        player.dir='left'
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


class run_down:
    @staticmethod
    def enter(player, e):
        player.wait_time =get_time()

    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame = (player.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 12

        if(player.y>120):
            player.y -= player.jump_speed * game_framework.frame_time

        if(player.y<120):
            player.y=120
            player.state_machine.handle_event(('TIME_OUT', 0))


    @staticmethod
    def render(player):
        if player.dir == 'left':
            player.idle_left_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)
        if player.dir == 'right':
            player.idle_right_image.clip_draw(int(player.frame) * 64, 0, 64, 86, player.x, player.y)

