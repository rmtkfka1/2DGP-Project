from pico2d import *


class player1:
    def __init__(self):
        self.x=1100
        self.y=100
        self.frame = 0
        self.image = load_image('1.png')
    def update(self):
        self.frame=(self.frame+1)%5

    def handle_event(self,e):
        if e.type==SDL_KEYDOWN and e.key == SDLK_SPACE:
            self.y+=10


    def render(self):
        self.image.clip_draw(self.frame*40,0,40,40,self.x,self.y,200,200)
