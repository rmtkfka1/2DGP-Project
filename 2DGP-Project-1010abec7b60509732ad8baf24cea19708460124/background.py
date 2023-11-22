from pico2d import *

class background:
    def __init__(self):
        self.x=1200//2
        self.y=700//2

        self.image = load_image('resource/bg.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(600,350)


class chair:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.image = load_image('resource/chair_front.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(self.x,self.y)

class safe_bar:
    def __init__(self):
        self.x=530
        self.y=335

        self.image = load_image('resource/safe_bar.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(self.x,self.y)


class p1_layer:
    def __init__(self):
        self.x=610
        self.y=365

        self.image = load_image('resource/p1_layer.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(self.x,self.y)

class p2_layer:
    def __init__(self):
        self.x=610
        self.y=200

        self.image = load_image('resource/p2_layer.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(self.x,self.y)



class ui:
    def __init__(self):
        self.x=600
        self.y=60

        self.image = load_image('resource/option1.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(self.x,self.y)


class logo:
    def __init__(self):
        self.x=600
        self.y=600

        self.image = load_image('resource/logo.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(self.x,self.y)

class select_background:
    def __init__(self):
        self.image = load_image('resource/select_background.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(600,350)


class select_background:
    def __init__(self):
        self.image = load_image('resource/select_background.png')

    def update(self):
        pass
    def handle_event(self,e):
        pass

    def render(self):
        self.image.draw(600,350)