from pico2d import *
import game_framework
import game_world

class Ball:
    def __init__(self):
        self.image =load_image('tennis_ball4.png')
        self.x=300
        self.y=200
        self.speed=100
        self.going_vector=(1,1)
        self.gravity =0

    def update(self):
        self.x += self.going_vector[0]
        self.y += self.going_vector[1]



        if self.x > 1200:
            reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1, 0)
            self.going_vector = reflection

        if self.x < 0:
            reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)
            self.going_vector = reflection

        if self.y > 700:
            reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, -1)
            self.going_vector = reflection

        if self.y < 100:
            reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, 1)
            self.going_vector = reflection


    def render(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x-20, self.y-20, self.x +20, self.y +20




