import random

from pico2d import load_image

import game_framework


class Audience:
    def __init__(self, ball, x, y):
        self.x = x
        self.y = y

        self.ball = ball

        # self.left_img = load_image("resource/1_left.png")
        self.left_img =[]
        self.right_img = []
        self.random_num =[]
        self.random_num.append(random.randint(3,14))
        self.random_num.append(random.randint(3,14))
        self.random_num.append(random.randint(3,14))
        self.random_num.append(random.randint(3,14))
        self.random_num.append(random.randint(3,14))



        for i in range(0,3):
            self.left_img.append(load_image("resource/Audience/" + str(i+1) + "_left.png"))

        for i in range(0, 3):
            self.right_img.append(load_image("resource/Audience/" + str(i+1) + "_right.png"))


    def update(self):
        pass

    def render(self):
        if self.ball.x <600:
            for i in range(3,14):
                if i == self.random_num[0] or i == self.random_num[1] or i == self.random_num[2] or  i == self.random_num[3]or  i == self.random_num[4]: continue
                j = i % 3
                self.left_img[j].draw(self.x+i*56,self.y)

        if self.ball.x >=600:
            for i in range(3,14):
                if i == self.random_num[0] or i == self.random_num[1] or i == self.random_num[2] or  i == self.random_num[3]or  i == self.random_num[4]: continue
                j = i % 3
                self.right_img[j].draw(self.x+ i*56,self.y)

    def get_bb(self):
        pass

    def handle_collusion(self, group, other):
        pass
