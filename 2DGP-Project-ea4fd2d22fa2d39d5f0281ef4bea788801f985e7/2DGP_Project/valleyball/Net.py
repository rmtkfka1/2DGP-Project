from pico2d import load_image, draw_rectangle

from share import game_world


class net:
    def __init__(self):
        self.x = 610
        self.y =80
        self.image = load_image('resource/balley/net.png')


    def update(self):
        pass


    def handle_event(self, event):
        pass


    def render(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())
        pass


    def get_bb(self):
        return self.x - 15, self.y - 80, self.x + 13, self.y + 150
        pass

    def handle_collusion(self, group, other):
        if group == "net:ball":
            if self.x < other.x:
                other.going_vector= game_world.normalize_vector(10, -10)

            if self.x > other.x:
                other.going_vector = game_world.normalize_vector(-10, -10)






