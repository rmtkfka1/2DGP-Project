from math import sqrt

from pico2d import *
import game_framework
import game_world
from player_state_machine import idle, jump


class Ball:
    def __init__(self):
        self.image =load_image('resource/tennis_ball4.png')
        # self.x=300
        self.x =1000
        self.y=200
        self.speed=1
        self.going_vector=self.speed * (500, 500)
        self.gravity = 1 # 중력 값 (원하는 값으로 조정)

    def update(self):
        self.x += self.speed * self.going_vector[0] * game_framework.frame_time
        self.y += self.speed * self.going_vector[1] * game_framework.frame_time

        self.going_vector = self.going_vector[0], self.going_vector[1] - self.gravity

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
                # if(self.going_vector[1] > 380 ):
                #     self.going_vector = self.going_vector[0],380


    def render(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x-20, self.y-20, self.x +20, self.y +20



    def handle_collusion(self,group,other):
        if group == "player1:ball":
            if (self.y > other.top):
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, 1)
                self.going_vector = reflection
                if (self.x < other.left):
                    self.x -= 5
                    return

                if (self.x >= other.right):
                    self.x += 5
                    return

            if (self.y < other.bottom):
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, -1)
                self.going_vector = reflection
                if (self.x < other.left):
                    self.x -= 5
                    return

                if (self.x >= other.right):
                    self.x += 5
                    return

            if other.top - self.y < 30:
                print("최상단 맞음")
                self.speed=0.8
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 60:
                print("상단 맞음")
                self.speed = 0.9
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 90:
                print("기운데 맞음")
                self.speed=1.2
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1,0)
                self.going_vector = reflection
                return

            if other.top - self.y < 120:
                print("하단 맞음")
                self.speed=0.9
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 150:
                print("최하단 맞음")
                self.speed=0.8
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], -1, 0)
                self.going_vector = reflection
                return


        if group == "player2:ball":

            if (self.y > other.top):
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, 1)
                self.going_vector = reflection
                if (self.x < other.left):
                    self.x -= 5
                    return

                if (self.x >= other.right):
                    self.x += 5
                    return

            if (self.y < other.bottom):
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 0, -1)
                self.going_vector = reflection
                if (self.x < other.left):
                    self.x -= 5
                    return

                if (self.x >= other.right):
                    self.x += 5
                    return

            if other.top - self.y < 30:
                print("최상단 맞음")
                self.speed = 0.8
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 60:
                print("상단 맞음")
                self.speed = 0.9
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 90:
                print("기운데 맞음")
                self.speed = 1.2
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 120:
                print("하단 맞음")
                self.speed = 0.9
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)
                self.going_vector = reflection
                return

            if other.top - self.y < 150:
                print("최하단 맞음")
                self.speed = 0.8
                reflection = game_world.reflection_vector(self.going_vector[0], self.going_vector[1], 1, 0)
                self.going_vector = reflection
                return

