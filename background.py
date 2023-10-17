from pico2d import *

class background:
    def __init__(self):
        self.x=1200//2
        self.y=700//2
        self.image = load_image('test.png')
    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(600,350)


