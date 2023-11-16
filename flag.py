from pico2d import load_image

import game_framework


class Flag:
    def __init__(self):
        self.red_x =20
        self.red_y= 570
        self.blue_x= 1180
        self.blue_y =570
        self.frame = 0
        self.red_flag_image = load_image('resource/red_flag.png')
        self.blue_flag_image = load_image('resource/blue_flag.png')
        self.frame=0


    def update(self):
        self.frame= (self.frame+ 10* game_framework.frame_time)%5


    def render(self):
        self.red_flag_image.clip_draw(200 * int(self.frame), 0, 200, 200, self.red_x, self.red_y)
        self.blue_flag_image.clip_draw(200*int(self.frame),0,200,200,self.blue_x,self.blue_y)

    def get_bb(self):
        pass

    def handle_collusion(self, group, other):
        pass

