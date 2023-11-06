from pico2d import get_time

import game_framework

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class idle:
    @staticmethod
    def enter(player, e):
        player.gravity = 1


    @staticmethod
    def exit(player, e):
        pass

    @staticmethod
    def update(player):
        player.frame_divide += 2
        if (player.frame_divide >= 1):
            if (player.frame == 0):
                player.frame = 0
            else:
                player.frame -= 1
            player.frame_divide = 0

        if(player.y>180):
            player.y -=  player.gravity*RUN_SPEED_PPS * game_framework.frame_time

        player.gravity += 3.0 * game_framework.frame_time



    @staticmethod
    def render(player):
        player.image.clip_draw(int(player.frame)*115,0,115,175,player.x,player.y)
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
        if (player.frame == 5):
            player.frame = 5
        else:
            player.frame += 1

        if(player.y <600):
            player.y += 300 * game_framework.frame_time

        if(get_time()- player.wait_time>0.3):
            player.state_machine.handle_event(('TIME_OUT',0))

    @staticmethod
    def render(player):
        player.image.clip_draw(int(player.frame)*115,0,115,175,player.x,player.y)
        pass
