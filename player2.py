from pico2d import *


class player2:
    def __init__(self):
        self.x=200
        self.y=180
        self.frame = 0
        self.image = load_image('p2_img.png')
    def update(self):
        self.frame=(self.frame+1)%5
    def handle_event(self,e):
        pass


    def render(self):
        self.image.clip_draw(self.frame*115,0,115,175,self.x,self.y)
