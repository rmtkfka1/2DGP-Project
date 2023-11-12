from pico2d import load_image

import game_world


class referee:
    def __init__(self,ball):
        self.x = 605
        self.y = 280
        self.frame = 0
        self.left_image = load_image('resource/ref_left.png')
        self.right_image = load_image('resource/ref_right.png')
        self.ball=ball

    def update(self):
        pass


    def render(self):
        if self.ball.x < 600:
            self.left_image.draw(self.x,self.y)

        else:
            self.right_image.draw(self.x, self.y)


    def get_bb(self):
        pass

    def handle_collusion(self, group, other):
        pass
